"""
KB Processor Module

This module orchestrates the KB article refresh workflow.
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

from tqdm import tqdm

# Add path handling for directories
# Get the base project directory (2 levels up from this script)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

from kb_refresh.pdf_extractor import get_extractor, PDFExtractor
from kb_refresh.chunker import DocumentChunker
from kb_refresh.embedder import TextEmbedder
from kb_refresh.html_processor import HTMLProcessor
from kb_refresh.llm_client import AzureOpenAIClient


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
        similarity_threshold: float = 0.5,
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
            product_name: Name of the product.

        Returns:
            Path to the saved embeddings.
        """
        # First, check for PDF in product-specific subfolder
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
        # Extract text with sections
        document = self.pdf_extractor.extract_text_with_sections(pdf_path)
        
        # Chunk the document
        chunked_doc = self.chunker.chunk_document(document)
        
        # Generate embeddings
        embedded_doc = self.embedder.generate_embeddings(chunked_doc)
        
        # Save embeddings
        embeddings_path = self.embedder.save_embeddings(
            embedded_doc, 
            f"{product_name}_embeddings.jsonl"
        )
        
        print(f"Saved embeddings to {embeddings_path}")
        return embeddings_path

    def find_relevant_chunks(
        self, 
        article_content: str, 
        embeddings_path: str
    ) -> List[Dict]:
        """
        Find chunks that are relevant to an article.

        Args:
            article_content: Content of the article.
            embeddings_path: Path to embeddings file.

        Returns:
            List of relevant document chunks.
        """
        # Load embeddings
        embedded_doc = self.embedder.load_embeddings(embeddings_path)
        chunks = embedded_doc.get("chunks", [])
        
        # Generate embedding for the article
        article_embedding = self.embedder.model.encode([article_content])[0].tolist()
        
        # Extract embeddings from chunks
        chunk_embeddings = [chunk["embedding"] for chunk in chunks]
        
        # Compute similarity
        similarities = self.embedder.compute_similarity(article_embedding, chunk_embeddings)
        
        # Sort chunks by similarity
        chunk_similarities = list(zip(chunks, similarities))
        chunk_similarities.sort(key=lambda x: x[1], reverse=True)
        
        # Filter chunks by similarity threshold
        relevant_chunks = [
            chunk for chunk, score in chunk_similarities 
            if score >= self.similarity_threshold
        ]
        
        # Limit to max chunks per article
        relevant_chunks = relevant_chunks[:self.max_chunks_per_article]
        
        return relevant_chunks

    def refresh_article(
        self, 
        article_path: str, 
        embeddings_path: str
    ) -> Tuple[str, bool]:
        """
        Refresh a KB article.

        Args:
            article_path: Path to the article.
            embeddings_path: Path to embeddings file.

        Returns:
            Tuple of (output path, outdated flag).
        """
        # Extract article content
        article = self.html_processor.extract_kb_article(article_path)
        
        # Find relevant chunks
        relevant_chunks = self.find_relevant_chunks(article["content"], embeddings_path)
        
        if not relevant_chunks:
            print(f"No relevant chunks found for {article['id']}.")
            return None, False
        
        # Refresh article with LLM
        refreshed_content, is_outdated = self.llm_client.refresh_article(
            article["content"], 
            relevant_chunks
        )
        
        # Save refreshed article
        output_path = self.html_processor.save_updated_article(
            article, 
            refreshed_content, 
            output_folder=self.output_dir
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
        report = "# KB Article Refresh Report\n\n"
        report += f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # Summary
        total_articles = sum(r["articles_processed"] for r in results)
        total_outdated = sum(r["articles_outdated"] for r in results)
        total_errors = sum(len(r["errors"]) for r in results)
        
        report += "## Summary\n\n"
        report += f"- **Total products processed:** {len(results)}\n"
        report += f"- **Total articles processed:** {total_articles}\n"
        report += f"- **Articles flagged as outdated:** {total_outdated} ({total_outdated/total_articles*100:.1f if total_articles > 0 else 0}%)\n"
        report += f"- **Processing errors:** {total_errors}\n\n"
        
        # Product details
        report += "## Product Details\n\n"
        
        for result in results:
            product = result["product"]
            articles = result["articles_processed"]
            outdated = result["articles_outdated"]
            
            report += f"### {product}\n\n"
            report += f"- **Articles processed:** {articles}\n"
            report += f"- **Articles flagged as outdated:** {outdated} ({outdated/articles*100:.1f if articles > 0 else 0}%)\n"
            
            if result["outdated_articles"]:
                report += "\n**Outdated Articles:**\n\n"
                for article in result["outdated_articles"]:
                    report += f"- {article}\n"
            
            if result["errors"]:
                report += "\n**Errors:**\n\n"
                for error in result["errors"]:
                    report += f"- {error}\n"
            
            report += "\n"
        
        # Save report
        report_path = os.path.join(self.output_dir, "refresh_report.md")
        with open(report_path, "w") as f:
            f.write(report)
        
        return report_path

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
    
    parser.add_argument(
        "--output-dir", 
        default="refreshed-articles",
        help="Directory to save refreshed articles (relative to project root)"
    )
    
    parser.add_argument(
        "--embedding-dir", 
        default="embeddings",
        help="Directory to save embeddings (relative to project root)"
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
        default=0.5,
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
    
    args = parser.parse_args()
    
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
    
    if args.product:
        processor.process_product(args.product, max_articles=args.max_articles)
    else:
        processor.process_all(max_articles=args.max_articles)


if __name__ == "__main__":
    main()
