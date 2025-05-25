import os
import re
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

class KBDuplicateDetector:
    def __init__(self, directory_path, similarity_threshold=0.7):
        self.directory_path = directory_path
        self.similarity_threshold = similarity_threshold
        self.articles = {}
        self.similarity_matrix = None
        
    def clean_text(self, text):
        """Clean and normalize text content."""
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', ' ', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters
        text = re.sub(r'[^\w\s]', '', text)
        return text.strip().lower()
    
    def extract_content(self, html_content):
        """Extract meaningful content from HTML."""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract title
        title = soup.find('title')
        title = title.text if title else ''
        
        # Extract main content
        content_div = soup.find('div', class_='Content__c')
        if not content_div:
            return title, ''
            
        # Extract text from all sections
        sections = []
        for section in content_div.find_all(['h2', 'h3', 'p', 'ul', 'ol']):
            sections.append(section.get_text())
            
        content = ' '.join(sections)
        return title, content
    
    def load_articles(self, specific_files=None):
        """
        Load and process HTML articles.
        
        Args:
            specific_files: List of specific files to process. If None, processes all files in directory.
        """
        if specific_files is None:
            # Process all files in the directory
            for root, _, files in os.walk(self.directory_path):
                for file in files:
                    if file.endswith('.html'):
                        file_path = os.path.join(root, file)
                        self._process_article_file(file_path)
        else:
            # Process only the specified files
            for file_path in specific_files:
                if os.path.isfile(file_path) and file_path.endswith('.html'):
                    self._process_article_file(file_path)
    
    def _process_article_file(self, file_path):
        """Process a single article file and add it to the articles dictionary."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
                title, content = self.extract_content(html_content)
                if content:
                    self.articles[file_path] = {
                        'title': title,
                        'content': self.clean_text(content)
                    }
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
    
    def calculate_similarity(self):
        """Calculate similarity between all articles."""
        if not self.articles:
            return
            
        # Create TF-IDF matrix
        vectorizer = TfidfVectorizer(stop_words='english')
        content_list = [article['content'] for article in self.articles.values()]
        tfidf_matrix = vectorizer.fit_transform(content_list)
        
        # Calculate cosine similarity
        self.similarity_matrix = cosine_similarity(tfidf_matrix)
    
    def most_similar_snippet(self, text1, text2, n=10):
        """Find the most similar n-gram snippet between two texts."""
        words1 = text1.split()
        words2 = text2.split()
        max_overlap = 0
        best_snippet = ("", "")
        
        # Create n-grams for both texts
        ngrams1 = [" ".join(words1[i:i+n]) for i in range(len(words1)-n+1)]
        ngrams2 = [" ".join(words2[i:i+n]) for i in range(len(words2)-n+1)]
        
        for ng1 in ngrams1:
            for ng2 in ngrams2:
                # Overlap: number of shared words
                overlap = len(set(ng1.split()) & set(ng2.split()))
                if overlap > max_overlap:
                    max_overlap = overlap
                    best_snippet = (ng1, ng2)
        return best_snippet

    def find_duplicates(self, modified_files=None):
        """
        Find potential duplicate articles.
        
        Args:
            modified_files: List of modified files to check against all other articles.
                          If None, checks all articles against each other.
        """
        if self.similarity_matrix is None:
            return []
            
        duplicates = []
        all_files = list(self.articles.keys())
        
        if modified_files:
            # Only check modified files against all other files
            modified_indices = [i for i, path in enumerate(all_files) if path in modified_files]
            
            for i in modified_indices:
                for j in range(len(all_files)):
                    # Skip self-comparison
                    if i == j:
                        continue
                        
                    similarity = self.similarity_matrix[i][j]
                    if similarity >= self.similarity_threshold:
                        snippet1, snippet2 = self.most_similar_snippet(
                            self.articles[all_files[i]]['content'],
                            self.articles[all_files[j]]['content']
                        )
                        duplicates.append({
                            'file1': all_files[i],  # The modified file
                            'file2': all_files[j],  # The potential duplicate
                            'similarity': similarity,
                            'title1': self.articles[all_files[i]]['title'],
                            'title2': self.articles[all_files[j]]['title'],
                            'snippet1': snippet1,
                            'snippet2': snippet2
                        })
        else:
            # Check all files against each other
            for i in range(len(all_files)):
                for j in range(i + 1, len(all_files)):
                    similarity = self.similarity_matrix[i][j]
                    if similarity >= self.similarity_threshold:
                        snippet1, snippet2 = self.most_similar_snippet(
                            self.articles[all_files[i]]['content'],
                            self.articles[all_files[j]]['content']
                        )
                        duplicates.append({
                            'file1': all_files[i],
                            'file2': all_files[j],
                            'similarity': similarity,
                            'title1': self.articles[all_files[i]]['title'],
                            'title2': self.articles[all_files[j]]['title'],
                            'snippet1': snippet1,
                            'snippet2': snippet2
                        })
        
        # Sort by similarity in descending order
        return sorted(duplicates, key=lambda x: x['similarity'], reverse=True)
    
    def generate_report(self, duplicates):
        """Generate a CSV report of potential duplicates."""
        if not duplicates:
            print("No potential duplicates found.")
            return None
            
        # Create a DataFrame from the duplicates list
        df = pd.DataFrame(duplicates)
        
        # Reorder columns for better readability
        df = df[['similarity', 'title1', 'file1', 'snippet1', 'title2', 'file2', 'snippet2']]
        
        # Format similarity as percentage
        df['similarity'] = df['similarity'].apply(lambda x: f"{x:.2%}")
        
        # Generate output filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"duplicate_articles_{timestamp}.csv"
        
        # Save to CSV
        df.to_csv(output_file, index=False)
        print(f"\nReport saved to: {output_file}")
        print(f"Found {len(duplicates)} potential duplicate pairs")
        
        return output_file

def ensure_directory_exists(directory):
    """Ensure the specified directory exists."""
    os.makedirs(directory, exist_ok=True)
    return directory

def save_json_report(data, directory, filename_prefix):
    """Save data as JSON file with timestamp in the specified directory."""
    import json
    from datetime import datetime
    import os
    
    # Ensure directory exists
    ensure_directory_exists(directory)
    
    # Create filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.json"
    filepath = os.path.join(directory, filename)
    
    # Save the file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    return filepath

def generate_n8n_output(duplicates, product_name, threshold, execution_time, articles_processed, save_to_file=True):
    """Generate n8n-compatible JSON output.
    
    Args:
        duplicates: List of duplicate article pairs
        product_name: Name of the product being analyzed
        threshold: Similarity threshold used
        execution_time: Time taken to run the analysis (seconds)
        articles_processed: Number of articles processed
        save_to_file: Whether to save the report to a file
        
    Returns:
        dict: The report data
    """
    from datetime import datetime
    import json
    import os
    
    # Convert file paths to forward slashes for consistency
    def normalize_path(path):
        if not path:
            return path
        path = os.path.normpath(path)
        return path.replace('\\', '/')
    
    # Prepare duplicates list with proper formatting
    duplicates_list = []
    for dup in duplicates:
        try:
            dup_item = {
                "file1": normalize_path(dup.get('file1', '')),
                "file2": normalize_path(dup.get('file2', '')),
                "similarity": round(float(dup.get('similarity', 0)), 4),
                "title1": dup.get('title1', ''),
                "title2": dup.get('title2', '')
            }
            
            # Add snippets if they exist
            if 'snippet1' in dup:
                snippet = str(dup['snippet1'])
                dup_item['snippet1'] = (snippet[:200] + '...') if len(snippet) > 200 else snippet
            if 'snippet2' in dup:
                snippet = str(dup['snippet2'])
                dup_item['snippet2'] = (snippet[:200] + '...') if len(snippet) > 200 else snippet
                
            duplicates_list.append(dup_item)
        except Exception as e:
            print(f"Error formatting duplicate item: {e}")
            continue
    
    # Prepare the report data
    report_data = {
        "status": "success" if not duplicates_list else "warning" if len(duplicates_list) < 5 else "error",
        "execution_details": {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "execution_time_seconds": round(execution_time, 3)
        },
        "request_details": {
            "product_requested": str(product_name) if product_name else "Unspecified",
            "similarity_threshold_used": float(threshold) if threshold is not None else 0.7
        },
        "results": {
            "articles_processed": int(articles_processed) if articles_processed is not None else 0,
            "potential_duplicates_found": len(duplicates_list),
            "potential_duplicates": duplicates_list
        }
    }
    
    return report_data

def parse_arguments():
    import argparse
    parser = argparse.ArgumentParser(description='Detect duplicate knowledge base articles.')
    parser.add_argument('--directory', type=str, default='kb-md',
                       help='Directory containing the knowledge base articles')
    parser.add_argument('--threshold', type=float, default=0.7,
                       help='Similarity threshold (0.0 to 1.0)')
    parser.add_argument('--output-format', type=str, 
                       choices=['csv', 'github', 'n8n'], default='csv',
                       help='Output format: csv, github, or n8n')
    parser.add_argument('--product-name', type=str, default='',
                       help='Product name for reporting purposes')
    return parser.parse_args()

def generate_github_report(duplicates, output_file='duplicate_articles_report.md'):
    """Generate a GitHub-flavored markdown report."""
    if not duplicates:
        with open(output_file, 'w') as f:
            f.write("## No duplicate articles found. ")
        return 0
    
    with open(output_file, 'w') as f:
        f.write("## Duplicate Articles Detected \n\n")
        f.write("The following articles have high similarity scores and might be duplicates. "
                "Please review them before merging.\n\n")
        f.write("| Similarity | Article 1 | Article 2 |\n")
        f.write("|------------|-----------|------------|\n")
        
        for dup in duplicates:
            # Create relative paths for better readability
            rel_path1 = os.path.relpath(dup['file1'])
            rel_path2 = os.path.relpath(dup['file2'])
            
            # Truncate titles if too long
            title1 = (dup['title1'][:50] + '...') if len(dup['title1']) > 50 else dup['title1']
            title2 = (dup['title2'][:50] + '...') if len(dup['title2']) > 50 else dup['title2']
            
            f.write(f"| {dup['similarity']:.1%} | "
                   f"[{title1}]({rel_path1}) | "
                   f"[{title2}]({rel_path2}) |\n")
        
        f.write("\n> Note: This is an automated check. Please review the articles to confirm if they are actual duplicates.\n")
    
    return len(duplicates)

def get_modified_files():
    """Get list of modified/added markdown files in the knowledge base."""
    import subprocess
    
    try:
        # Get list of modified/added files in the PR
        cmd = ["git", "diff", "--name-only", "--diff-filter=ACMRT", "HEAD^1", "HEAD"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Filter for markdown files in the knowledge base
        modified_files = [
            f.strip() for f in result.stdout.split('\n') 
            if f.strip().endswith(('.md', '.mdx')) and f.strip().startswith('knowledge_base/')
        ]
        
        return modified_files
    except Exception as e:
        print(f"Error getting modified files: {e}")
        return []

def main():
    import time
    import json
    import os
    import sys
    
    start_time = time.time()
    args = parse_arguments()
    
    # Get list of modified files
    modified_files = get_modified_files()
    
    if modified_files:
        print(f"Found {len(modified_files)} modified files to check:")
        for f in modified_files:
            print(f"  - {f}")
    else:
        print("No modified markdown files found in the knowledge base.")
        if args.output_format == 'n8n':
            result = {
                "status": "success",
                "execution_details": {
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "execution_time_seconds": round(time.time() - start_time, 3)
                },
                "request_details": {
                    "product_requested": args.product_name or "All Products",
                    "similarity_threshold_used": args.threshold
                },
                "results": {
                    "articles_processed": 0,
                    "potential_duplicates_found": 0,
                    "potential_duplicates": []
                }
            }
            print(json.dumps(result, indent=2))
        return
    
    # Create detector instance for the entire knowledge base
    detector = KBDuplicateDetector('knowledge_base', similarity_threshold=args.threshold)
    
    # Process all articles in the knowledge base
    print("Loading all articles from the knowledge base...")
    detector.load_articles()
    print(f"Loaded {len(detector.articles)} articles")
    
    # Prepare base result for empty case
    if not detector.articles:
        print("No articles found. Exiting.")
        if args.output_format == 'n8n':
            result = {
                "status": "success",
                "execution_details": {
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "execution_time_seconds": round(time.time() - start_time, 3)
                },
                "request_details": {
                    "product_requested": args.product_name or "Unspecified",
                    "similarity_threshold_used": args.threshold
                },
                "results": {
                    "articles_processed": 0,
                    "potential_duplicates_found": 0,
                    "potential_duplicates": []
                }
            }
            # Save the report to the reports directory
            reports_dir = os.path.join('reports', 'duplicate_prevention')
            report_path = save_json_report(
                result, 
                reports_dir,
                f"duplicates_{args.product_name.lower().replace(' ', '_') if args.product_name else 'report'}"
            )
            print(f"\nReport saved to: {report_path}")
            print(json.dumps(result, indent=2))
        return
    
    # Calculate similarities
    print("Calculating similarities...")
    detector.calculate_similarity()
    
    # Find duplicates for modified files
    print("Checking for duplicates against the entire knowledge base...")
    duplicates = detector.find_duplicates(modified_files=modified_files)
    
    # Calculate execution time
    execution_time = time.time() - start_time
    
    # Generate appropriate output
    if args.output_format == 'github':
        num_duplicates = generate_github_report(duplicates)
        if num_duplicates > 0:
            print(f"\nFound {num_duplicates} potential duplicate pairs. Report generated.")
            # Exit with error code if duplicates found (will fail the GitHub Action)
            exit(1)
        else:
            print("\nNo duplicate articles found.")
    elif args.output_format == 'n8n':
        result = generate_n8n_output(
            duplicates=duplicates,
            product_name=args.product_name or os.path.basename(os.path.normpath(args.directory)),
            threshold=args.threshold,
            execution_time=execution_time,
            articles_processed=len(detector.articles)
        )
        
        # Save the report to the reports directory
        reports_dir = os.path.join('reports', 'duplicate_prevention')
        report_path = save_json_report(
            result, 
            reports_dir,
            f"duplicates_{args.product_name.lower().replace(' ', '_') if args.product_name else 'report'}"
        )
        print(f"\nReport saved to: {report_path}")
        
        # Also print to stdout for GitHub Actions
        print(json.dumps(result, indent=2))
        
        # Exit with error code if duplicates found (for GitHub Actions)
        if duplicates:
            exit(1)
    else:
        detector.generate_report(duplicates)

if __name__ == "__main__":
    main()