"""
KB Processor Module

This module orchestrates the KB article refresh workflow.
"""

import os
import argparse
import glob
import json
import logging
import os
import re
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union, Any
from tqdm import tqdm
from dataclasses import dataclass, field
from sentence_transformers import SentenceTransformer, LoggingHandler
from bs4 import BeautifulSoup, Tag
import numpy as np
import pdfplumber

# Configure logging to suppress unnecessary messages
logging.basicConfig(
    level=logging.ERROR,  # Only show ERROR level and above
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.NullHandler()  # This will suppress all logging
    ]
)

# Suppress specific logger
logging.getLogger('sentence_transformers').setLevel(logging.ERROR)
logging.getLogger('pdfplumber').setLevel(logging.ERROR)
logging.getLogger('PIL').setLevel(logging.ERROR)

# Add path handling for directories
# Get the base project directory (2 levels up from this script)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

from pdf_extractor import get_extractor, PDFExtractor
from chunker import DocumentChunker
from embedder import TextEmbedder
from html_processor import HTMLProcessor
from llm_client import AzureOpenAIClient

class KBProcessor:
    """Main processor for KB article refresh."""

    def __init__(
        self,
        pdf_dir: str = "doc-pdfs",
        html_dir: str = "all-articles-html",
        output_dir: str = "refreshed-articles",
        embedding_dir: str = "embeddings",
        embedder_model: str = "all-MiniLM-L6-v2",
        pdf_backend: str = "pypdf2",
        max_chunks_per_article: int = 5,
        similarity_threshold: float = 0.3,
    ):
        """
        Initialize the KB processor.

        Args:
            pdf_dir: Directory containing PDF files.
            html_dir: Directory containing HTML KB articles.
            output_dir: Directory to save refreshed articles.
            embedding_dir: Directory to save embeddings.
            embedder_model: Name of the sentence-transformer model to use.
            pdf_backend: Name of the PDF extraction backend.
            max_chunks_per_article: Maximum number of document chunks to use per article.
            similarity_threshold: Minimum similarity score for retrieving chunks.
        """
        # Convert to absolute paths based on the project root
        self.pdf_dir = os.path.join(BASE_DIR, pdf_dir)
        self.html_dir = os.path.join(BASE_DIR, html_dir)
        self.output_dir = os.path.join(BASE_DIR, output_dir)
        self.embedding_dir = os.path.join(BASE_DIR, embedding_dir)
        
        # Initialize components
        self.pdf_extractor = get_extractor(backend=pdf_backend)
        self.chunker = DocumentChunker()
        self.embedder = TextEmbedder(model_name=embedder_model, output_dir=embedding_dir)
        self.html_processor = HTMLProcessor(base_dir=html_dir)
        self.llm_client = AzureOpenAIClient()
        
        self.max_chunks_per_article = max_chunks_per_article
        self.similarity_threshold = similarity_threshold
        
        # Create output directories
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(embedding_dir, exist_ok=True)

    def process_pdfs(self, product_name: str) -> str:
        """
        Process PDFs for a product.

        Args:
            product_name: Name of the product or full PDF file name (without extension).

        Returns:
            Path to the saved embeddings, or None if processing failed.
        """
        # Check if product_name is actually a file name (contains "netwrix_")
        is_filename = "netwrix_" in product_name
        
        # First, check if embeddings file already exists
        embeddings_filename = f"{product_name}_embeddings.jsonl"
        embeddings_path = os.path.join(self.embedding_dir, embeddings_filename)
        
        if os.path.exists(embeddings_path):
            print(f"Embeddings file already exists at {embeddings_path}. Checking if it's valid...")
            try:
                # Try to load the embeddings to verify they're valid
                embedded_doc = self.embedder.load_embeddings(embeddings_path)
                if embedded_doc and "chunks" in embedded_doc and len(embedded_doc["chunks"]) > 0:
                    print("Existing embeddings file is valid. Using existing embeddings.")
                    return embeddings_path
                else:
                    print("Existing embeddings file is empty or invalid. Regenerating...")
            except Exception as e:
                print(f"Error loading existing embeddings: {e}. Regenerating...")
        
        # If we get here, need to process the PDF
        print(f"No valid embeddings found for {product_name}. Processing PDF...")
        
        # If product_name is actually a file name, adjust the search path
        if is_filename:
            # First try to find in the pdf_dir
            pdf_path = os.path.join(self.pdf_dir, f"{product_name}.pdf")
            if not os.path.exists(pdf_path):
                # Try with just the file name
                potential_pdfs = []
                if os.path.exists(self.pdf_dir):
                    for file in os.listdir(self.pdf_dir):
                        if file.endswith(".pdf") and product_name in file:
                            potential_pdfs.append(os.path.join(self.pdf_dir, file))
                
                # Also search in subdirectories of pdf_dir
                for root, _, files in os.walk(self.pdf_dir):
                    for file in files:
                        if file.endswith(".pdf") and product_name in file:
                            potential_pdfs.append(os.path.join(root, file))
                
                if potential_pdfs:
                    pdf_path = potential_pdfs[0]
                    print(f"Found PDF file: {pdf_path}")
        else:
            # First, check for PDF in product-specific subfolder (original behavior)
            product_pdf_dir = os.path.join(self.pdf_dir, product_name)
            pdf_path = None
            
            # Debug information
            print(f"Looking for PDFs in: {self.pdf_dir}")
            print(f"Looking for product-specific PDFs in: {product_pdf_dir}")
            
            if os.path.exists(product_pdf_dir) and os.path.isdir(product_pdf_dir):
                print(f"Found product directory at {product_pdf_dir}")
                # Try to find any PDF in the product-specific directory
                potential_pdfs = [
                    os.path.join(product_pdf_dir, file)
                    for file in os.listdir(product_pdf_dir)
                    if file.endswith(".pdf")
                ]
                if potential_pdfs:
                    pdf_path = potential_pdfs[0]
                    print(f"Using product-specific PDF: {pdf_path}")
            else:
                # Try in the main PDF directory
                pdf_path = os.path.join(self.pdf_dir, f"{product_name}.pdf")
        
        if pdf_path is None or not os.path.exists(pdf_path):
            if pdf_path is not None:
                print(f"PDF not found at {pdf_path}. Looking for alternative PDFs...")
            # Try to find any PDF in the directory with this product name in its filename
            base_pdf_pattern = product_name.replace('-', '_').lower()
            
            potential_pdfs = []
            if os.path.exists(self.pdf_dir):
                for file in os.listdir(self.pdf_dir):
                    if file.endswith(".pdf"):
                        lowercase_file = file.lower()
                        # Check for various naming patterns
                        if base_pdf_pattern in lowercase_file or product_name in lowercase_file:
                            potential_pdfs.append(os.path.join(self.pdf_dir, file))
                
            if not potential_pdfs:
                print(f"No PDFs found for {product_name}.")
                return None
                
            pdf_path = potential_pdfs[0]
            print(f"Found alternative PDF: {pdf_path}")
            
        print(f"Processing PDF: {pdf_path}")
        
        # Define paths for chunked and extracted files
        base_filename = os.path.splitext(os.path.basename(pdf_path))[0]
        
        # Check for existing chunked file in the chunked directory
        chunked_dir = os.path.join(os.path.dirname(__file__), "chunked")
        extracted_dir = os.path.join(os.path.dirname(__file__), "extracted")
        os.makedirs(chunked_dir, exist_ok=True)
        os.makedirs(extracted_dir, exist_ok=True)
        
        chunked_path = os.path.join(chunked_dir, f"{base_filename}_chunked.json")
        extracted_path = os.path.join(extracted_dir, f"{base_filename}_extracted.txt")
        
        chunked_doc = None
        
        # Check if chunked file exists and is valid
        if os.path.exists(chunked_path):
            print(f"Found existing chunked file at {chunked_path}")
            try:
                with open(chunked_path, 'r', encoding='utf-8') as f:
                    chunked_doc = json.load(f)
                if not chunked_doc or "chunks" not in chunked_doc or not chunked_doc["chunks"]:
                    print("Existing chunked file is empty or invalid. Regenerating...")
                    chunked_doc = None
                else:
                    print(f"Using existing chunked file with {len(chunked_doc['chunks'])} chunks")
            except Exception as e:
                print(f"Error loading chunked file: {e}. Regenerating...")
                chunked_doc = None
        
        # If we don't have valid chunks, try to load from extracted text
        if chunked_doc is None and os.path.exists(extracted_path):
            print(f"Found existing extracted text at {extracted_path}")
            try:
                with open(extracted_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                
                # Create document structure from extracted text
                document = {
                    "product_name": product_name,
                    "sections": [{
                        "section_name": "Main Content",
                        "text": text,
                        "page_range": [1, 1],
                        "level": 1
                    }]
                }
                
                # Chunk the document
                print("Chunking document from extracted text...")
                chunked_doc = self.chunker.chunk_document(document)
                
                # Save the chunked document
                with open(chunked_path, 'w', encoding='utf-8') as f:
                    json.dump(chunked_doc, f, indent=2, ensure_ascii=False)
                print(f"Saved chunked document to {chunked_path}")
                
            except Exception as e:
                print(f"Error processing extracted text: {e}")
                chunked_doc = None
        
        # If we still don't have chunks, extract from PDF
        if chunked_doc is None:
            print("Extracting text from PDF...")
            try:
                document = self.pdf_extractor.extract_text_with_sections(pdf_path)
                
                # Save extracted text for future use
                if hasattr(document, 'get') and 'sections' in document and document['sections']:
                    os.makedirs(os.path.dirname(extracted_path), exist_ok=True)
                    with open(extracted_path, 'w', encoding='utf-8') as f:
                        f.write(document['sections'][0].get('text', ''))
                
                # Chunk the document
                print("Chunking document from PDF...")
                chunked_doc = self.chunker.chunk_document(document)
                
                # Save the chunked document
                with open(chunked_path, 'w', encoding='utf-8') as f:
                    json.dump(chunked_doc, f, indent=2, ensure_ascii=False)
                print(f"Saved chunked document to {chunked_path}")
                
            except Exception as e:
                print(f"Error processing PDF: {e}")
                return None
        
        # Generate embeddings
        print("Generating embeddings...")
        try:
            embedded_doc = self.embedder.generate_embeddings(chunked_doc)
            
            # Save embeddings
            print(f"Saving embeddings to {embeddings_path}")
            embeddings_path = self.embedder.save_embeddings(
                embedded_doc, 
                embeddings_filename
            )
            
            print(f"Successfully processed and saved embeddings to {embeddings_path}")
            return embeddings_path
            
        except Exception as e:
            print(f"Error generating or saving embeddings: {e}")
            return None

    def find_relevant_chunks(
        self, 
        article_content: str, 
        embeddings_path: str
    ) -> Tuple[List[Dict], List[Dict]]:
        """
        Find chunks that are relevant to an article.

        Args:
            article_content: Content of the article.
            embeddings_path: Path to embeddings file.

        Returns:
            Tuple of (list of relevant chunks, list of chunks with scores)
        """
        # Load embeddings
        embedded_doc = self.embedder.load_embeddings(embeddings_path)
        chunks = embedded_doc.get("chunks", [])
        
        if not chunks:
            print("Warning: No chunks found in the embeddings file.")
            return [], []
            
        # Generate embedding for the article
        article_embedding = self.embedder.model.encode([article_content])[0].tolist()
        
        # Extract embeddings from chunks and ensure they are in the correct format
        chunk_embeddings = []
        valid_chunks = []
        
        for chunk in chunks:
            if "embedding" in chunk and chunk["embedding"]:
                chunk_embeddings.append(chunk["embedding"])
                valid_chunks.append(chunk)
        
        if not chunk_embeddings:
            print("Warning: No valid embeddings found in chunks.")
            return [], []
            
        # Ensure embeddings are in the correct format (2D array)
        chunk_embeddings = np.array(chunk_embeddings)
        if len(chunk_embeddings.shape) == 1:
            chunk_embeddings = chunk_embeddings.reshape(1, -1)
        
        # Compute similarity
        try:
            similarities = self.embedder.compute_similarity(article_embedding, chunk_embeddings)
        except Exception as e:
            print(f"Error computing similarities: {e}")
            print(f"Embeddings shape: {chunk_embeddings.shape}")
            print(f"Article embedding shape: {np.array(article_embedding).shape}")
            return [], []
        
        # Create chunks with scores
        chunks_with_scores = []
        for chunk, score in zip(valid_chunks, similarities):
            chunk_with_score = chunk.copy()
            chunk_with_score["similarity_score"] = float(score)  # Convert numpy float to Python float
            chunks_with_scores.append(chunk_with_score)
        
        # Sort chunks by similarity
        chunks_with_scores.sort(key=lambda x: x["similarity_score"], reverse=True)
        
        # Filter chunks by similarity threshold and limit to max chunks
        relevant_chunks = [
            {k: v for k, v in chunk.items() if k != 'embedding'}  # Remove the embedding to save space
            for chunk in chunks_with_scores 
            if chunk["similarity_score"] >= self.similarity_threshold
        ][:self.max_chunks_per_article]
        
        return relevant_chunks, chunks_with_scores

    def refresh_article(
        self, 
        article_path: str, 
        embeddings_path: str,
        output_dir: Optional[str] = None
    ) -> Tuple[str, bool]:
        """
        Refresh a KB article.

        Args:
            article_path: Path to the article.
            embeddings_path: Path to embeddings file.
            output_dir: Directory to save the refreshed article. If None, uses the instance's output_dir.

        Returns:
            Tuple of (output path, outdated flag).
        """
        # Extract article content
        article = self.html_processor.extract_kb_article(article_path)
        
        # Find relevant chunks and get chunks with scores
        relevant_chunks, all_chunks_with_scores = self.find_relevant_chunks(article["content"], embeddings_path)
        
        if not relevant_chunks:
            print(f"No relevant chunks found for {article.get('id', 'unknown')}.")
            return None, False
        
        # Save reference chunks to JSON file
        output_dir = output_dir or self.output_dir
        article_id = article.get('id', os.path.splitext(os.path.basename(article_path))[0])
        reference_file = os.path.join(output_dir, f"{article_id}_reference.json")
        
        # Prepare reference data with only relevant chunks
        reference_data = {
            'article_id': article_id,
            'article_path': os.path.abspath(article_path),
            'embedding_file': os.path.abspath(embeddings_path),
            'processed_at': datetime.now().isoformat(),
            'relevant_chunks': relevant_chunks
        }
        
        try:
            with open(reference_file, 'w', encoding='utf-8') as f:
                json.dump(reference_data, f, indent=2, ensure_ascii=False)
            print(f"Saved reference chunks to: {reference_file}")
        except Exception as e:
            print(f"Error saving reference chunks: {e}")
        
        # Refresh article with LLM
        refreshed_content, is_outdated = self.llm_client.refresh_article(
            article["content"], 
            relevant_chunks
        )
        
        # Save refreshed article
        output_path = self.html_processor.save_updated_article(
            article, 
            refreshed_content, 
            output_folder=output_dir
        )
        
        return output_path, is_outdated

    def process_product(self, product_name: str, max_articles: Optional[int] = None) -> Dict:
        """
        Process a product (PDF and KB articles).

        Args:
            product_name: Name of the product.
            max_articles: Maximum number of articles to process (for testing).

        Returns:
            Dictionary with processing results.
        """
        results = {
            "product": product_name,
            "timestamp": datetime.now().isoformat(),
            "articles_processed": 0,
            "articles_outdated": 0,
            "refreshed_articles": [],
            "outdated_articles": [],
            "errors": []
        }
        
        # Process PDFs
        embeddings_path = self.process_pdfs(product_name)
        if not embeddings_path:
            results["errors"].append(f"No PDF found for {product_name}")
            return results
        
        # Process KB articles
        article_paths = self.html_processor.get_kb_articles(product_name)
        
        # Limit the number of articles if max_articles is specified
        if max_articles is not None:
            print(f"Limiting to {max_articles} articles for testing")
            article_paths = article_paths[:max_articles]
            
        for article_path in tqdm(article_paths, desc=f"Processing articles for {product_name}"):
            try:
                output_path, is_outdated = self.refresh_article(article_path, embeddings_path)
                
                results["articles_processed"] += 1
                
                if is_outdated:
                    results["articles_outdated"] += 1
                    results["outdated_articles"].append(os.path.basename(article_path))
                    
                results["refreshed_articles"].append(os.path.basename(output_path))
                
            except Exception as e:
                print(f"Error processing article {article_path}: {e}")
                results["errors"].append(f"Error processing {os.path.basename(article_path)}: {str(e)}")
        
        # Save results
        results_path = os.path.join(self.output_dir, f"{product_name}_results.json")
        with open(results_path, "w") as f:
            json.dump(results, f, indent=2)
        
        return results

    def generate_report(self, results: List[Dict]) -> str:
        """
        Generate a Markdown report from processing results.

        Args:
            results: List of product processing results.

        Returns:
            Path to the generated report.
        """
        if not results:
            print("No results to generate report from.")
            return ""
            
        report = "# KB Article Refresh Report\n\n"
        report += f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # Calculate summary statistics
        total_products = len(results)
        total_articles = sum(r.get("articles_processed", 0) for r in results)
        total_outdated = sum(r.get("articles_outdated", 0) for r in results)
        total_errors = sum(len(r.get("errors", [])) for r in results)
        
        # Add summary section
        report += "## Summary\n\n"
        report += f"- **Total products processed:** {total_products}\n"
        report += f"- **Total articles processed:** {total_articles}\n"
        
        # Safely calculate outdated percentage
        if total_articles > 0:
            outdated_percent = (total_outdated / total_articles) * 100
            report += f"- **Articles flagged as outdated:** {total_outdated} ({outdated_percent:.1f}%)\n"
        else:
            report += "- **Articles flagged as outdated:** 0 (0.0%)\n"
            
        if total_errors > 0:
            report += f"- **Total errors encountered:** {total_errors}\n"
        
        # Add detailed results section
        report += "\n## Detailed Results\n\n"
        
        for result in results:
            product_name = result.get("product", "Unknown Product")
            articles_processed = result.get("articles_processed", 0)
            articles_outdated = result.get("articles_outdated", 0)
            
            report += f"### {product_name}\n"
            report += f"- **Articles processed:** {articles_processed}\n"
            
            if articles_processed > 0:
                outdated_pct = (articles_outdated / articles_processed) * 100
                report += f"- **Outdated articles:** {articles_outdated} ({outdated_pct:.1f}%)\n"
            
            # List outdated articles if any
            outdated_articles = result.get("outdated_articles", [])
            if outdated_articles:
                report += "\n**Outdated Articles:**\n"
                for article in outdated_articles:
                    report += f"- {article}\n"
            
            # List errors if any
            errors = result.get("errors", [])
            if errors:
                report += "\n**Errors:**\n"
                for error in errors:
                    report += f"- {error}\n"
            
            report += "\n"
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Save report to file
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_path = os.path.join(self.output_dir, f"kb_refresh_report_{timestamp}.md")
        
        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"✅ Report generated: {report_path}")
            return report_path
        except Exception as e:
            print(f"⚠️  Error saving report: {e}")
            return ""

    def process_all(self, max_articles: Optional[int] = None) -> str:
        """
        Process all products.

        Args:
            max_articles: Maximum number of articles to process per product (for testing).

        Returns:
            Path to the generated report.
        """
        print("Starting KB article refresh process...")
        
        # Get all product folders
        product_folders = self.html_processor.get_product_folders()
        
        results = []
        for product in tqdm(product_folders, desc="Processing products"):
            print(f"\nProcessing product: {product}")
            result = self.process_product(product, max_articles=max_articles)
            results.append(result)
        
        # Generate report
        report_path = self.generate_report(results)
        
        print(f"\nProcess complete. Report saved to {report_path}")
        return report_path


def main():
    """Main entry point for the KB article refresh tool."""
    parser = argparse.ArgumentParser(description="KB Article Refresh Tool")
    
    parser.add_argument(
        "--pdf-dir", 
        default="doc-pdfs",
        help="Directory containing PDF files (relative to project root)"
    )
    
    parser.add_argument(
        "--html-dir", 
        default="all-articles-html",
        help="Directory containing HTML KB articles (relative to project root)"
    )
    
    # Set different default for output-dir if extract flags are used
    output_dir_default = "refreshed-articles"
    
    parser.add_argument(
        "--output-dir", 
        default=output_dir_default,
        help="Directory to save outputs (relative to project root)"
    )
    
    parser.add_argument(
        "--embedding-dir", 
        default="embeddings",
        help="Directory to save embeddings (relative to project root)"
    )
    
    parser.add_argument(
        "--embeddings-path",
        help="Direct path to a specific embeddings file (overrides automatic embeddings detection)"
    )
    
    parser.add_argument(
        "--embedder-model", 
        default="all-MiniLM-L6-v2",
        help="Name of the sentence-transformer model to use"
    )
    
    parser.add_argument(
        "--pdf-backend", 
        default="pypdf2",
        choices=["pypdf2", "pdfplumber"],
        help="PDF extraction backend to use"
    )
    
    parser.add_argument(
        "--max-chunks", 
        type=int,
        default=5,
        help="Maximum number of document chunks to use per article"
    )
    
    parser.add_argument(
        "--similarity-threshold", 
        type=float,
        default=0.3,
        help="Minimum similarity score for retrieving chunks"
    )
    
    parser.add_argument(
        "--product", 
        help="Process a specific product (omit to process all)"
    )
    
    parser.add_argument(
        "--max-articles",
        type=int,
        help="Maximum number of articles to process per product (for testing)"
    )
    
    parser.add_argument(
        "--article-ids",
        help="Comma-separated list of specific article IDs to process (e.g., '12345,67890')"
    )
    
    # New arguments for step-by-step pipeline testing
    parser.add_argument(
        "--pdf-path",
        help="Specific PDF file to process (absolute path)"
    )
    
    parser.add_argument(
        "--extract-only",
        action="store_true",
        help="Just extract text from PDF and save to a text file"
    )
    
    parser.add_argument(
        "--extract-and-chunk",
        action="store_true",
        help="Extract text from PDF, chunk it, and save chunks to a JSON file"
    )
    
    parser.add_argument(
        "--extract-chunk-embed",
        action="store_true",
        help="Extract text, chunk it, generate embeddings, and save to an embedding file"
    )
    
    parser.add_argument(
        "--article-path",
        help="Specific article file to process (absolute path) or directory containing articles"
    )
    
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Process HTML files in subdirectories when using --article-path with a directory"
    )
    
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit processing to the first N articles in a directory"
    )
    
    args = parser.parse_args()
    
    # Fast path for extract-only operations - bypass embeddings search
    if args.extract_only and args.pdf_path:
        # Process the PDF for extraction only
        extracted_dir = os.path.join(BASE_DIR, "kb-config", "kb_refresh", "extracted")
        os.makedirs(extracted_dir, exist_ok=True)
        
        if os.path.isfile(args.pdf_path):
            print(f"Processing PDF: {args.pdf_path}")
            try:
                # Extract text from PDF
                extractor = PDFExtractor()
                text = extractor.extract_text(args.pdf_path)
                
                # Save extracted text
                output_filename = f"{os.path.splitext(os.path.basename(args.pdf_path))[0]}_extracted.txt"
                output_path = os.path.join(extracted_dir, output_filename)
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                
                print(f"Successfully extracted text to: {output_path}")
            except Exception as e:
                print(f"Error processing PDF: {e}")
                import traceback
                traceback.print_exc()
        elif os.path.isdir(args.pdf_path):
            print(f"Looking for PDFs in: {args.pdf_path}")
            pdf_files = glob.glob(os.path.join(args.pdf_path, "*.pdf"))
            if pdf_files:
                for pdf_file in pdf_files:
                    print(f"Processing PDF: {pdf_file}")
                    try:
                        # Extract text from PDF
                        extractor = PDFExtractor()
                        text = extractor.extract_text(pdf_file)
                        
                        # Save extracted text
                        output_filename = f"{os.path.splitext(os.path.basename(pdf_file))[0]}_extracted.txt"
                        output_path = os.path.join(extracted_dir, output_filename)
                        
                        with open(output_path, 'w', encoding='utf-8') as f:
                            f.write(text)
                        
                        print(f"Successfully extracted text to: {output_path}")
                    except Exception as e:
                        print(f"Error processing {pdf_file}: {e}")
                        continue
            else:
                print(f"No PDF files found in {args.pdf_path}")
        else:
            print(f"Error: {args.pdf_path} is not a valid file or directory")
        return
    
    # Set default output directory to 'extracted' if --extract-only is used and no output-dir provided
    if (args.extract_only or args.extract_and_chunk or args.extract_chunk_embed) and not args.output_dir:
        args.output_dir = os.path.join(BASE_DIR, "kb-config", "kb_refresh", "extracted")
    
    processor = KBProcessor(
        pdf_dir=args.pdf_dir,
        html_dir=args.html_dir,
        output_dir=args.output_dir,
        embedding_dir=args.embedding_dir,
        embedder_model=args.embedder_model,
        pdf_backend=args.pdf_backend,
        max_chunks_per_article=args.max_chunks,
        similarity_threshold=args.similarity_threshold
    )
    
    # If embeddings path is directly specified, use it
    embeddings_path = None
    if args.embeddings_path:
        if os.path.exists(args.embeddings_path):
            embeddings_path = args.embeddings_path
            print(f"Using specified embeddings file: {embeddings_path}")
        else:
            print(f"Error: Specified embeddings file not found at {args.embeddings_path}")
            return
    
    # Handle direct PDF and article processing
    if args.pdf_path and args.article_path:
        # Make sure the files exist
        if not os.path.exists(args.pdf_path):
            print(f"Error: PDF file not found at {args.pdf_path}")
            return
            
        if not os.path.exists(args.article_path):
            print(f"Error: Article file not found at {args.article_path}")
            return
            
        # Define paths
        base_name = os.path.splitext(os.path.basename(args.pdf_path))[0]
        
        # Define all possible directories to check for existing files
        base_dirs = [
            os.path.join(BASE_DIR, "kb-config", "kb_refresh"),  # Local kb-config directory
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),  # Project root
            os.getcwd()  # Current working directory
        ]
        
        # Look for existing files in all directories if embeddings_path not already set
        if embeddings_path is None:
            chunked_path = None
            extracted_path = None
            
            # Check for existing files in all directories
            for base_dir in base_dirs:
                # Check for embeddings
                possible_embeddings = os.path.join(base_dir, "embeddings", f"{base_name}_embeddings.jsonl")
                if not embeddings_path and os.path.exists(possible_embeddings):
                    embeddings_path = possible_embeddings
                    print(f"Found existing embeddings at: {embeddings_path}")
                
                # Check for chunked file
                possible_chunked = os.path.join(base_dir, "chunked", f"{base_name}_chunked.json")
                if not chunked_path and os.path.exists(possible_chunked):
                    chunked_path = possible_chunked
                    print(f"Found existing chunked file at: {chunked_path}")
                
                # Check for extracted text
                possible_extracted = os.path.join(base_dir, "extracted", f"{base_name}_extracted.txt")
                if not extracted_path and os.path.exists(possible_extracted):
                    extracted_path = possible_extracted
                    print(f"Found existing extracted text at: {extracted_path}")
        
        # Determine if we need to process the PDF
        process_pdf = True
        
        # Ensure embeddings_path is a string and exists
        if embeddings_path:
            embeddings_path = str(embeddings_path)  # Ensure it's a string
            if os.path.exists(embeddings_path):
                try:
                    # Try to load the embeddings to verify they're valid
                    with open(embeddings_path, 'r', encoding='utf-8') as f:
                        first_line = f.readline()
                        if first_line:
                            print(f"Using existing embeddings from: {embeddings_path}")
                            process_pdf = False
                        else:
                            print("Warning: Empty embeddings file. Will regenerate.")
                except Exception as e:
                    print(f"Warning: Error reading embeddings file: {e}. Will regenerate.")
            else:
                print(f"Warning: Embeddings file not found at {embeddings_path}. Will generate new embeddings.")
        else:
            print("No embeddings path specified. Will generate new embeddings.")
            # Set a default path for new embeddings
            embeddings_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "embeddings", f"{base_name}_embeddings.jsonl")
        
        # Process PDF if needed
        if process_pdf:
            # Create necessary directories if they don't exist
            local_dirs = [
                os.path.join(BASE_DIR, "kb-config", "kb_refresh", "chunked"),
                os.path.join(BASE_DIR, "kb-config", "kb_refresh", "extracted"),
                os.path.join(BASE_DIR, "kb-config", "kb_refresh", "embeddings"),
                "chunked",
                "extracted",
                "embeddings"
            ]
            
            for dir_path in local_dirs:
                os.makedirs(dir_path, exist_ok=True)
            
            # Set default paths if not found in the search
            if not chunked_path:
                chunked_path = os.path.join(BASE_DIR, "kb-config", "kb_refresh", "chunked", f"{base_name}_chunked.json")
            if not extracted_path:
                extracted_path = os.path.join(BASE_DIR, "kb-config", "kb_refresh", "extracted", f"{base_name}_extracted.txt")
            if not embeddings_path:
                embeddings_path = os.path.join(BASE_DIR, "kb-config", "kb_refresh", "embeddings", f"{base_name}_embeddings.jsonl")
            
            chunked_doc = None
            
            # Check if chunked file exists and is valid
            if os.path.exists(chunked_path):
                print(f"Found existing chunked file at {chunked_path}")
                try:
                    with open(chunked_path, 'r', encoding='utf-8') as f:
                        chunked_doc = json.load(f)
                    if not chunked_doc or "chunks" not in chunked_doc or not chunked_doc["chunks"]:
                        print("Existing chunked file is empty or invalid. Regenerating...")
                        chunked_doc = None
                    else:
                        print(f"Using existing chunked file with {len(chunked_doc['chunks'])} chunks")
                except Exception as e:
                    print(f"Error loading chunked file: {e}. Regenerating...")
                    chunked_doc = None
            
            # If we don't have valid chunks, try to load from extracted text
            if chunked_doc is None and os.path.exists(extracted_path):
                print(f"Found existing extracted text at {extracted_path}")
                try:
                    with open(extracted_path, 'r', encoding='utf-8') as f:
                        text = f.read()
                    
                    # Create document structure from extracted text
                    document = {
                        "product_name": base_name,
                        "sections": [{
                            "section_name": "Main Content",
                            "text": text,
                            "page_range": [1, 1],
                            "level": 1
                        }]
                    }
                    
                    # Chunk the document
                    print("Chunking document from extracted text...")
                    chunked_doc = processor.chunker.chunk_document(document)
                    
                    # Save the chunked document
                    with open(chunked_path, 'w', encoding='utf-8') as f:
                        json.dump(chunked_doc, f, indent=2, ensure_ascii=False)
                    print(f"Saved chunked document to {chunked_path}")
                    
                except Exception as e:
                    print(f"Error processing extracted text: {e}")
                    chunked_doc = None
            
            # If we still don't have chunks, extract from PDF
            if chunked_doc is None:
                print("Extracting text from PDF...")
                try:
                    document = processor.pdf_extractor.extract_text_with_sections(args.pdf_path)
                    
                    # Save extracted text for future use
                    if hasattr(document, 'get') and 'sections' in document and document['sections']:
                        os.makedirs(os.path.dirname(extracted_path), exist_ok=True)
                        with open(extracted_path, 'w', encoding='utf-8') as f:
                            f.write(document['sections'][0].get('text', ''))
                    
                    # Chunk the document
                    print("Chunking document from PDF...")
                    chunked_doc = processor.chunker.chunk_document(document)
                    
                    # Save the chunked document
                    with open(chunked_path, 'w', encoding='utf-8') as f:
                        json.dump(chunked_doc, f, indent=2, ensure_ascii=False)
                    print(f"Saved chunked document to {chunked_path}")
                    
                except Exception as e:
                    print(f"Error processing PDF: {e}")
                    return
            
            # Generate embeddings
            print("Generating embeddings...")
            try:
                embedded_doc = processor.embedder.generate_embeddings(chunked_doc)
                
                # Save embeddings
                print(f"Saving embeddings to {embeddings_path}")
                embeddings_path = processor.embedder.save_embeddings(
                    embedded_doc, 
                    os.path.basename(embeddings_path)
                )
                print(f"Successfully processed and saved embeddings to {embeddings_path}")
                
            except Exception as e:
                print(f"Error generating or saving embeddings: {e}")
                return
                
            # Save embeddings to all relevant directories
            embedding_dirs = [
                os.path.join(BASE_DIR, "kb-config", "kb_refresh", "embeddings"),
                "embeddings"
            ]
            
            # Ensure we have a valid embeddings path
            if not embeddings_path:
                embeddings_path = os.path.join(embedding_dirs[0], f"{base_name}_embeddings.jsonl")
                os.makedirs(os.path.dirname(embeddings_path), exist_ok=True)
            
            # Save to all directories
            saved_paths = []
            for embed_dir in embedding_dirs:
                os.makedirs(embed_dir, exist_ok=True)
                current_path = os.path.join(embed_dir, f"{base_name}_embeddings.jsonl")
                with open(current_path, 'w', encoding='utf-8') as f:
                    for chunk in embedded_doc['chunks']:
                        f.write(json.dumps(chunk) + '\n')
                saved_paths.append(current_path)
                print(f"Embeddings saved to: {current_path}")
            
            # Use the first saved path as the main embeddings path
            if saved_paths:
                embeddings_path = saved_paths[0]
            
            # If article-path was provided, process the article now that we have embeddings
            if args.article_path:
                print(f"\nProcessing article {args.article_path} with the generated embeddings...")
                try:
                    # Set output directory to be the same as the input article
                    article_dir = os.path.dirname(os.path.abspath(args.article_path))
                    try:
                        output_path, is_outdated = processor.refresh_article(
                            args.article_path, 
                            embeddings_path,
                            output_dir=article_dir  # Pass the article's directory as output directory
                        )
                        if output_path:
                            print(f"Article processed. Output saved to: {output_path}")
                            print(f"Article flagged as outdated: {is_outdated}")
                        else:
                            print("Error: Failed to save the processed article")
                    except Exception as e:
                        print(f"Error processing article: {e}")
                        import traceback
                        traceback.print_exc()
                except Exception as e:
                    print(f"Error processing article: {e}")
                    import traceback
                    traceback.print_exc()
            return
    
    # Run specific article refresh if article path is provided
    if args.article_path and embeddings_path is None:
        # Get the directory containing the article(s)
        article_dir = os.path.dirname(args.article_path) if os.path.isfile(args.article_path) else args.article_path
        
        # Look for PDFs in this directory
        pdf_matches = glob.glob(os.path.join(article_dir, "netwrix_*.pdf"))
        if pdf_matches:
            pdf_path = pdf_matches[0]  # Use the first matching PDF
            print(f"Found PDF at: {pdf_path}")
            
            # Extract the base name to find or generate embeddings
            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            possible_embeddings = os.path.join(BASE_DIR, "kb-config", "kb_refresh", "embeddings", f"{base_name}_embeddings.jsonl")
            
            if os.path.exists(possible_embeddings):
                embeddings_path = possible_embeddings
                print(f"Found embeddings file at: {embeddings_path}")
            else:
                # Process the PDF to generate embeddings
                # Use the article directory as the output directory to save processed files in the same location
                processor = KBProcessor(
                    pdf_dir=os.path.dirname(pdf_path),
                    html_dir=os.path.dirname(article_dir) if os.path.isfile(args.article_path) else article_dir,
                    output_dir=article_dir,  # Save processed articles in the same directory
                    embedder_model=args.embedder_model,
                    pdf_backend=args.pdf_backend,
                    max_chunks_per_article=args.max_chunks,
                    similarity_threshold=args.similarity_threshold
                )
                
                # Generate embeddings from the PDF using the actual PDF basename
                product_name = base_name
                embeddings_path = processor.process_pdfs(product_name)
            
                if not embeddings_path:
                    print("Error: Failed to generate embeddings from PDF")
                    return
        else:
            print("Error: No PDF found in the article directory")
            return
    else:
        # Only look for existing embeddings if embeddings_path is not already set
        if embeddings_path is None:
            base_dirs = [
                os.path.join(BASE_DIR, "kb-config", "kb_refresh"),
                os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                os.getcwd()
            ]
            
            for base_dir in base_dirs:
                # Look for embeddings with different naming patterns
                possible_patterns = [
                    os.path.join(base_dir, "embeddings", "*_embeddings.jsonl"),
                    os.path.join(base_dir, "embeddings", "*.jsonl")  # Fallback to any JSONL file
                ]
                
                for pattern in possible_patterns:
                    matches = glob.glob(pattern)
                    if matches:
                        embeddings_path = matches[0]  # Use the first match
                        print(f"Found embeddings at: {embeddings_path}")
                        break
                if embeddings_path:
                    break
            
            if not embeddings_path:
                print("Error: No embeddings found and no PDF provided to generate them")
                return
    
    # Initialize processor
    processor = KBProcessor(
        pdf_dir=args.pdf_dir,
        html_dir=args.html_dir,
        output_dir=args.output_dir,
        embedder_model=args.embedder_model,
        pdf_backend=args.pdf_backend,
        max_chunks_per_article=args.max_chunks,
        similarity_threshold=args.similarity_threshold
    )

    # Process based on arguments
    if args.article_path:
        # Process a single article or directory of articles
        article_path = os.path.abspath(args.article_path)
        
        if os.path.isdir(article_path):
            # Process all articles in directory
            process_article_directory(
                processor,
                article_path,
                embeddings_path=embeddings_path,
                recursive=args.recursive,
                limit=args.limit
            )
        elif os.path.isfile(article_path):
            # Process single article
            process_article(
                processor,
                article_path,
                embeddings_path=embeddings_path
            )
        else:
            print(f"Error: {article_path} is not a valid file or directory")
            return
    elif hasattr(args, 'article_ids') and args.article_ids:
        # Process specific articles by ID
        for article_id in args.article_ids:
            article_path = os.path.join(processor.html_dir, f"{article_id}.html")
            if os.path.exists(article_path):
                process_article(
                    processor,
                    article_path,
                    embeddings_path=embeddings_path
                )
            else:
                print(f"Warning: Article {article_id} not found at {article_path}")
    elif hasattr(args, 'product') and args.product:
        # Process a specific product
        processor.process_product(args.product, args.max_articles)
    elif args.extract_only or args.extract_and_chunk or args.extract_chunk_embed:
        # Now we only handle extract_and_chunk and extract_chunk_embed here
        # extract_only is handled in the early fast path
        if args.pdf_path:
            # Skip extract-only as it's already handled
            if args.extract_and_chunk or args.extract_chunk_embed:
                # Define directories
                extracted_dir = os.path.join(BASE_DIR, "kb-config", "kb_refresh", "extracted")
                chunked_dir = os.path.join(BASE_DIR, "kb-config", "kb_refresh", "chunked")
                embeddings_dir = os.path.join(BASE_DIR, "kb-config", "kb_refresh", "embeddings")

                # Create directories if they don't exist
                os.makedirs(extracted_dir, exist_ok=True)
                os.makedirs(chunked_dir, exist_ok=True)
                if args.extract_chunk_embed:
                    os.makedirs(embeddings_dir, exist_ok=True)
                
                # Process a single PDF file
                if os.path.isfile(args.pdf_path):
                    base_filename = os.path.splitext(os.path.basename(args.pdf_path))[0]
                    extracted_path = os.path.join(extracted_dir, f"{base_filename}_extracted.txt")
                    chunked_path = os.path.join(chunked_dir, f"{base_filename}_chunked.json")
                    embeddings_path = os.path.join(embeddings_dir, f"{base_filename}_embeddings.jsonl")

                    print(f"Processing PDF: {args.pdf_path}")
                    
                    # Step 1: Check for existing extraction or extract text
                    extracted_text = None
                    if os.path.exists(extracted_path):
                        print(f"Found existing extraction at {extracted_path}")
                        try:
                            with open(extracted_path, 'r', encoding='utf-8') as f:
                                extracted_text = f.read()
                            print("Successfully loaded existing extraction")
                        except Exception as e:
                            print(f"Error loading existing extraction: {e}")
                            extracted_text = None
                    
                    # If no valid extraction was found, extract the text
                    if not extracted_text:
                        try:
                            extractor = PDFExtractor()
                            extracted_text = extractor.extract_text(args.pdf_path)
                            
                            # Save extracted text
                            with open(extracted_path, 'w', encoding='utf-8') as f:
                                f.write(extracted_text)
                            print(f"Successfully extracted text to: {extracted_path}")
                        except Exception as e:
                            print(f"Error extracting text: {e}")
                            import traceback
                            traceback.print_exc()
                            return
                    
                    # Step 2: Perform chunking if requested
                    if args.extract_and_chunk or args.extract_chunk_embed:
                        # Check for existing chunked file
                        chunked_doc = None
                        if os.path.exists(chunked_path):
                            print(f"Found existing chunked file at {chunked_path}")
                            try:
                                with open(chunked_path, 'r', encoding='utf-8') as f:
                                    chunked_doc = json.load(f)
                                if not chunked_doc or "chunks" not in chunked_doc or not chunked_doc["chunks"]:
                                    print("Existing chunked file is empty or invalid. Regenerating...")
                                    chunked_doc = None
                                else:
                                    print(f"Using existing chunked file with {len(chunked_doc['chunks'])} chunks")
                            except Exception as e:
                                print(f"Error loading chunked file: {e}. Regenerating...")
                                chunked_doc = None
                        
                        # If no valid chunked document was found, create one
                        if not chunked_doc:
                            # Create document structure for chunker
                            document = {
                                "product_name": base_filename,
                                "sections": [{
                                    "section_name": "Main Content",
                                    "text": extracted_text,
                                    "page_range": [1, 1],
                                    "level": 1
                                }]
                            }
                            
                            # Chunk the document
                            print("Chunking document...")
                            try:
                                chunker = DocumentChunker()
                                chunked_doc = chunker.chunk_document(document)
                                
                                # Save the chunked document
                                with open(chunked_path, 'w', encoding='utf-8') as f:
                                    json.dump(chunked_doc, f, indent=2, ensure_ascii=False)
                                print(f"Saved chunked document to {chunked_path}")
                            except Exception as e:
                                print(f"Error chunking document: {e}")
                                import traceback
                                traceback.print_exc()
                                return
                        
                        # Step 3: Generate embeddings if requested
                        if args.extract_chunk_embed and chunked_doc:
                            # Check if embeddings already exist
                            if os.path.exists(embeddings_path):
                                print(f"Found existing embeddings at {embeddings_path}")
                                # You could add code to verify embeddings here if needed
                            else:
                                print("Generating embeddings...")
                                try:
                                    embedder = TextEmbedder(output_dir=embeddings_dir)
                                    embedded_doc = embedder.generate_embeddings(chunked_doc)
                                    
                                    # Save embeddings
                                    embeddings_path = embedder.save_embeddings(
                                        embedded_doc, 
                                        f"{base_filename}_embeddings.jsonl"
                                    )
                                    print(f"Successfully saved embeddings to {embeddings_path}")
                                except Exception as e:
                                    print(f"Error generating embeddings: {e}")
                                    import traceback
                                    traceback.print_exc()
                                    return

                # Process a directory of PDF files
                elif os.path.isdir(args.pdf_path):
                    print(f"Looking for PDFs in: {args.pdf_path}")
                    pdf_files = glob.glob(os.path.join(args.pdf_path, "*.pdf"))
                    if pdf_files:
                        for pdf_file in pdf_files:
                            # Process each PDF the same way we process individual PDFs
                            # (Just process them one-by-one to avoid code duplication)
                            print(f"\nProcessing PDF: {pdf_file}")
                            # Call this same function recursively with the individual PDF
                            saved_args_pdf_path = args.pdf_path
                            args.pdf_path = pdf_file
                            # Re-run the current branch with the specific PDF file
                            if args.extract_and_chunk:
                                args.extract_and_chunk = True
                            if args.extract_chunk_embed:
                                args.extract_chunk_embed = True
                            main()
                            # Restore the original args.pdf_path for the next iteration
                            args.pdf_path = saved_args_pdf_path
                        print("\nCompleted processing all PDFs in directory.")
                        return
                    else:
                        print(f"No PDF files found in {args.pdf_path}")
                else:
                    print(f"Error: {args.pdf_path} is not a valid file or directory")
    else:
        # Process all products
        processor.process_all(args.max_articles)


def process_article(processor, article_path: str, embeddings_path: str) -> bool:
    """Process a single article.
    
    Args:
        processor: KBProcessor instance
        article_path: Path to the article file
        embeddings_path: Path to the embeddings file
        
    Returns:
        bool: True if processing was successful, False otherwise
    """
    article_name = os.path.basename(article_path)
    print(f"\nProcessing article: {article_name}")
    try:
        # Set output directory to be the same as the input article
        article_dir = os.path.dirname(article_path)
        
        # Check if the article has already been processed (revised version exists)
        revised_path = os.path.join(article_dir, article_name.replace('.html', '_revised.html'))
        if os.path.exists(revised_path):
            print(f"  ⏩ Skipping - already processed: {article_name}")
            return False
            
        output_path, is_outdated = processor.refresh_article(
            article_path, 
            embeddings_path,
            output_dir=article_dir
        )
        
        if output_path:
            print(f"  ✓ Processed. Output: {os.path.basename(output_path)}")
            print(f"  - Outdated: {is_outdated}")
            return True
        else:
            print("  ✗ Error: No relevant content found or failed to process article")
            return False
            
    except Exception as e:
        error_msg = str(e)
        if "No relevant chunks found" in error_msg:
            print(f"  ⚠️  Warning: No relevant content found in the knowledge base for {article_name}")
        else:
            print(f"  ✗ Error processing article: {error_msg}")
            import traceback
            traceback.print_exc()
        return False


def process_article_directory(processor, directory: str, embeddings_path: str, recursive: bool = False, limit: int = None) -> None:
    """Process all HTML articles in a directory.
    
    Args:
        processor: KBProcessor instance
        directory: Directory containing articles
        embeddings_path: Path to the embeddings file
        recursive: Whether to process subdirectories
        limit: Maximum number of articles to process
        
    Returns:
        dict: Processing statistics
    """
    print(f"Processing articles in directory: {directory}")
    if recursive:
        print("Recursive mode: ON (processing subdirectories)")
    if limit:
        print(f"Limit: Processing only the first {limit} articles")
    
    # Initialize counters
    stats = {
        'total': 0,
        'processed': 0,
        'skipped': 0,
        'no_content': 0,
        'errors': 0,
        'outdated': 0,
        'up_to_date': 0
    }
    
    # Get list of files to process
    files_to_process = []
    for root, _, files in os.walk(directory):
        if not recursive and root != directory:
            continue
            
        for file in files:
            if file.lower().endswith('.html') and not file.endswith('_revised.html'):
                article_path = os.path.join(root, file)
                files_to_process.append(article_path)
    
    # Apply limit if specified
    if limit and limit > 0 and limit < len(files_to_process):
        print(f"Limiting to first {limit} of {len(files_to_process)} articles")
        files_to_process = files_to_process[:limit]
    
    # Process files with progress bar
    if not files_to_process:
        print("\nNo HTML files found to process.")
        return stats
        
    print(f"\nFound {len(files_to_process)} articles to process...")
    
    for article_path in tqdm(files_to_process, desc="Processing articles"):
        stats['total'] += 1
        
        # Process the article
        result = process_article(processor, article_path, embeddings_path)
        
        # Update statistics
        if result is None:
            stats['skipped'] += 1
        elif result:
            stats['processed'] += 1
            # Check if the article was marked as outdated
            revised_path = article_path.replace('.html', '_revised.html')
            if os.path.exists(revised_path):
                with open(revised_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if 'outdated: true' in content.lower():
                        stats['outdated'] += 1
                    else:
                        stats['up_to_date'] += 1
        else:
            stats['errors'] += 1
    
    # Print summary
    print("\n" + "="*50)
    print("PROCESSING SUMMARY")
    print("="*50)
    print(f"Total articles found:    {stats['total']}")
    print(f"Successfully processed:  {stats['processed']}")
    if stats['skipped'] > 0:
        print(f"Skipped (already processed): {stats['skipped']}")
    if stats['no_content'] > 0:
        print(f"No relevant content:     {stats['no_content']}")
    if stats['errors'] > 0:
        print(f"Errors:                  {stats['errors']}")
    print("-"*50)
    if stats['processed'] > 0:
        print(f"Articles marked as outdated: {stats['outdated']}")
        print(f"Articles up to date:        {stats['up_to_date']}")
    print("="*50)
    
    return stats


if __name__ == "__main__":
    main()
