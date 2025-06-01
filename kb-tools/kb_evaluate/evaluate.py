#!/usr/bin/env python3
"""
KB Article Evaluation Script

Evaluates KB articles against documentation and generates assessment reports.
"""

import argparse
import os
import json
import glob
import datetime
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from tqdm import tqdm

# Import modules from kb_enhance if needed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Also add current directory to path for local imports
sys.path.append(os.path.dirname(__file__))
from kb_enhance.embedder import TextEmbedder
from kb_enhance.html_processor import HTMLProcessor

# Import local modules
from assessor import ArticleAssessor
from reporter import ReportGenerator

def main():
    # Ensure we're running from the project root directory
    project_root = find_project_root()
    os.chdir(project_root)
    print(f"Working directory: {os.getcwd()}")
    
    parser = argparse.ArgumentParser(description="Evaluate KB articles against documentation")
    parser.add_argument("--folder", help="Product folder to evaluate")
    parser.add_argument("--file", help="A single file in the product folder to determine which product to evaluate")
    parser.add_argument("--output-dir", default=".reports", help="Output directory for reports")
    parser.add_argument("--embeddings-dir", default=os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs_references", "embeddings"), 
                        help="Directory containing embeddings")
    parser.add_argument("--limit", type=int, help="Limit the number of articles to process (for testing)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    parser.add_argument("--duplicate-threshold", type=float, default=0.75, 
                       help="Similarity threshold for detecting potential duplicate articles (0.0-1.0)")
    parser.add_argument("--skip-duplicates", action="store_true", 
                       help="Skip checking for duplicate articles (faster)")
    args = parser.parse_args()
    
    verbose = args.verbose
    
    # Determine the product folder - either from args.folder or by parsing args.file
    product_folder = args.folder
    
    if not product_folder and args.file:
        # Extract product folder from file path
        file_path = os.path.abspath(args.file)
        
        # Check if this is in the all-articles-html structure
        if "all-articles-html" in file_path:
            # Split the path and look for the product folder
            path_parts = file_path.split(os.sep)
            try:
                html_index = path_parts.index("all-articles-html")
                if len(path_parts) > html_index + 1:
                    product_folder = path_parts[html_index + 1]
                    if verbose:
                        print(f"Auto-detected product folder: {product_folder}")
            except ValueError:
                pass
    
    if not product_folder:
        print("Error: No product folder specified. Use --folder or --file")
        return 1
        
    print(f"Evaluating product: {product_folder}")
        
    # Initialize components
    embedder = TextEmbedder(output_dir=args.embeddings_dir)
    html_processor = HTMLProcessor(base_dir="all-articles-html")
    
    # Get all HTML files in the product folder
    product_path = os.path.join("all-articles-html", product_folder)
    html_files = glob.glob(os.path.join(product_path, "*.html"))
    if args.limit:
        html_files = html_files[:args.limit]

    if not html_files:
        print(f"No HTML files found in {product_path}")
        return 1
    
    print(f"Found {len(html_files)} articles in {product_folder}")
        
    # Find embeddings for this product
    embeddings_file = find_embeddings_for_product(product_folder, args.embeddings_dir)
    if not embeddings_file:
        print(f"Error: No embeddings found for product folder {product_folder}")
        return 1
    
    # Initialize assessor and reporter
    assessor = ArticleAssessor()
    reporter = ReportGenerator(output_dir=".reports")
    
    # First, collect all article contents for duplicate detection
    all_articles = []
    article_embeddings = {}
    
    if not args.skip_duplicates:
        print("Collecting article content and generating embeddings for duplicate detection...")
        for html_file in tqdm(html_files, desc="Preprocessing articles"):
            try:
                # Extract article content and metadata
                article = html_processor.extract_kb_article(html_file, debug=False)
                
                # Add to all_articles
                all_articles.append({
                    "path": html_file,
                    "title": article["title"],
                    "content": article["content"]
                })
                
                # Generate embedding for this article
                article_embedding = embedder.model.encode([article["content"]])[0]
                article_embeddings[html_file] = article_embedding
                
            except Exception as e:
                print(f"Error processing {html_file} for duplicate detection: {e}")
    
    print(f"Processing {len(html_files)} KB articles...")

    # Process each article
    assessments = []
    for html_file in tqdm(html_files, desc="Assessing articles"):
        try:
            # Extract article content and metadata
            article = html_processor.extract_kb_article(html_file, debug=False)
            
            # Get creation and modification dates from metadata
            created_date, modified_date = extract_dates_from_article(html_file)
            
            # Find relevant chunks
            relevant_chunks = find_relevant_chunks(embedder, article["content"], embeddings_file)
            if verbose:
                print(f"Found {len(relevant_chunks)} relevant chunks for {os.path.basename(html_file)}")
            
            # Check for potential duplicates
            potential_duplicates = []
            if not args.skip_duplicates:
                potential_duplicates = find_potential_duplicates_with_precomputed_embeddings(
                    html_file,
                    all_articles,
                    article_embeddings,
                    embedder,
                    threshold=args.duplicate_threshold
                )
                
                if potential_duplicates and verbose:
                    print(f"Found {len(potential_duplicates)} potential duplicate articles for {os.path.basename(html_file)}")
                    for dup in potential_duplicates:
                        print(f"  - {os.path.basename(dup['path'])}: {dup['similarity_score']:.2f} similarity")
            
            # Assess the article
            assessment = assessor.assess_article(
                article_path=html_file,
                article_content=article["content"],
                article_title=article["title"],
                created_date=created_date,
                modified_date=modified_date,
                relevant_chunks=relevant_chunks
            )
            
            # Add potential duplicates to the assessment
            assessment["potential_duplicates"] = potential_duplicates
            
            assessments.append(assessment)
            
        except Exception as e:
            if verbose:
                print(f"Error processing {html_file}: {e}")
            # Add error assessment
            assessments.append({
                "article_path": html_file,
                "title": os.path.basename(html_file),
                "status": "error",
                "error_message": str(e),
                "priority": "unknown",
                "potential_duplicates": []
            })
            
    # Generate report
    print("Generating report...")
    report_path = reporter.generate_report(product_folder, assessments)
    
    print(f"\nEvaluation complete! Report saved to: {report_path}")
    return 0

def find_embeddings_for_product(product_folder: str, embeddings_dir: str) -> Optional[str]:
    """Find embeddings file for a product."""
    print(f"Looking for embeddings for {product_folder} in {embeddings_dir}")
    
    # Try multiple approaches to find matching embeddings
    product_name_clean = product_folder.replace('-', '_').lower()
    
    # Search patterns - try multiple variations
    patterns = [
        # Direct match with the product folder name
        os.path.join(embeddings_dir, f"{product_name_clean}*.jsonl"),
        os.path.join(embeddings_dir, f"*{product_name_clean}*.jsonl"),
        
        # Try with "netwrix_" prefix (common in documentation)
        os.path.join(embeddings_dir, f"netwrix_{product_name_clean}*.jsonl"),
        os.path.join(embeddings_dir, f"*netwrix_{product_name_clean}*.jsonl"),
        
        # Try with parts of the product name (for compound product names)
        *[os.path.join(embeddings_dir, f"*{part}*.jsonl") 
          for part in product_name_clean.split('_') if len(part) > 3]
    ]
    
    # Debug: List all files in the embeddings directory
    if os.path.exists(embeddings_dir):
        print(f"Files in {embeddings_dir}:")
        for file in os.listdir(embeddings_dir):
            print(f"  - {file}")
    else:
        print(f"Warning: Embeddings directory {embeddings_dir} does not exist")
    
    # Try each pattern
    for pattern in patterns:
        matches = glob.glob(pattern)
        if matches:
            print(f"Found embeddings file: {os.path.basename(matches[0])}")
            return matches[0]
    
    print("No matching embeddings file found.")
    return None

def extract_dates_from_article(html_file: str) -> Tuple[Optional[str], Optional[str]]:
    """Extract creation and modification dates from article metadata."""
    created_date = None
    modified_date = None
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract dates from meta tags
        import re
        created_match = re.search(r'<meta content="([^"]+)" name="createddate"/>', content)
        if created_match:
            created_date = created_match.group(1)
        
        modified_match = re.search(r'<meta content="([^"]+)" name="lastmodifieddate"/>', content)
        if modified_match:
            modified_date = modified_match.group(1)
    except Exception as e:
        print(f"Error extracting dates from {html_file}: {e}")
    
    return created_date, modified_date

def find_relevant_chunks(embedder, article_content, embeddings_file, max_chunks=5, threshold=0.3):
    """Find chunks from embeddings that are relevant to the article."""
    # Load embeddings
    embedded_doc = embedder.load_embeddings(embeddings_file)
    chunks = embedded_doc.get("chunks", [])
    
    if not chunks:
        return []
        
    # Generate embedding for the article
    article_embedding = embedder.model.encode([article_content])[0].tolist()
    
    # Extract embeddings from chunks
    chunk_embeddings = []
    valid_chunks = []
    
    for chunk in chunks:
        if "embedding" in chunk and chunk["embedding"]:
            chunk_embeddings.append(chunk["embedding"])
            valid_chunks.append(chunk)
    
    if not chunk_embeddings:
        return []
        
    # Compute similarity
    import numpy as np
    chunk_embeddings = np.array(chunk_embeddings)
    article_embedding = np.array(article_embedding)
    
    similarities = embedder.compute_similarity(article_embedding, chunk_embeddings)
    
    # Create chunks with scores
    chunks_with_scores = []
    for chunk, score in zip(valid_chunks, similarities):
        chunk_with_score = chunk.copy()
        chunk_with_score["similarity_score"] = float(score)
        chunks_with_scores.append(chunk_with_score)
    
    # Sort chunks by similarity and filter by threshold
    chunks_with_scores.sort(key=lambda x: x["similarity_score"], reverse=True)
    relevant_chunks = [
        {k: v for k, v in chunk.items() if k != 'embedding'}
        for chunk in chunks_with_scores 
        if chunk["similarity_score"] >= threshold
    ][:max_chunks]
    
    return relevant_chunks

def find_project_root():
    """Find the project root directory (where README.md is located)"""
    current_dir = os.path.abspath(os.path.dirname(__file__))
    
    # Traverse up until we find README.md or hit the root
    while True:
        if os.path.exists(os.path.join(current_dir, "README.md")):
            return current_dir
        
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # Reached root
            # Fall back to assuming we start 2 levels down from project root
            return os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
        
        current_dir = parent_dir

def find_potential_duplicates_with_precomputed_embeddings(
    article_path: str, 
    all_articles: List[Dict], 
    article_embeddings: Dict[str, List[float]],
    embedder,
    threshold: float = 0.75
) -> List[Dict]:
    """
    Find potential duplicate articles using precomputed embeddings.
    
    Args:
        article_path: Path to the current article
        all_articles: List of all articles to compare against
        article_embeddings: Dictionary of precomputed embeddings
        embedder: TextEmbedder instance to use for similarity calculation
        threshold: Similarity threshold for duplicate detection
        
    Returns:
        List of potentially duplicate articles with similarity scores
    """
    import numpy as np
    
    # Get embedding for the current article
    try:
        if article_path not in article_embeddings:
            return []
            
        article_embedding = article_embeddings[article_path]
        
        # Create a list to store potential duplicates
        potential_duplicates = []
        
        # Get the normalized path of the current article for exact matching
        normalized_current_path = os.path.normpath(os.path.abspath(article_path))
        
        # Compare with all other articles
        for article in all_articles:
            other_path = article["path"]
            
            # Normalize the other path for comparison
            normalized_other_path = os.path.normpath(os.path.abspath(other_path))
            
            # Skip comparing with self (using normalized paths for reliable comparison)
            if normalized_other_path == normalized_current_path:
                continue
                
            # Skip if no embedding for the other article
            if other_path not in article_embeddings:
                continue
                
            other_embedding = article_embeddings[other_path]
            
            # Calculate cosine similarity
            similarity = embedder.compute_similarity(
                article_embedding, 
                other_embedding.reshape(1, -1)
            )[0]
            
            # If similarity is above threshold, add to potential duplicates
            if similarity >= threshold:
                potential_duplicates.append({
                    "path": other_path,
                    "title": article["title"],
                    "similarity_score": float(similarity)
                })
        
        # Sort by similarity score (highest first)
        potential_duplicates.sort(key=lambda x: x["similarity_score"], reverse=True)
        
        return potential_duplicates
    
    except Exception as e:
        print(f"Error checking for duplicates: {e}")
        return []

if __name__ == "__main__":
    sys.exit(main()) 