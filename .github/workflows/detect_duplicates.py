import os
import re
import argparse
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

class KBDuplicateDetector:
    def __init__(self, directory_path, similarity_threshold=0.7):
        # Convert to absolute path and normalize
        self.directory_path = os.path.abspath(os.path.normpath(directory_path))
        print(f"\nInitializing detector with directory: {self.directory_path}")
        print(f"Directory exists: {os.path.exists(self.directory_path)}")
        print(f"Is directory: {os.path.isdir(self.directory_path) if os.path.exists(self.directory_path) else 'N/A'}")
        
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
        Load and process articles (HTML, MDX, or MD files).
        
        Args:
            specific_files: List of specific files to process. If None, processes all files in directory.
        """
        if specific_files is None:
            # Process all files in the directory, including hidden directories
            for root, dirs, files in os.walk(self.directory_path):
                # Include hidden directories (those starting with .)
                dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('node_modules', '__pycache__')]
                
                print(f"\nScanning directory: {root}")
                print(f"Found {len(files)} files")
                
                for file in files:
                    if file.endswith(('.html', '.mdx', '.md')):
                        file_path = os.path.join(root, file)
                        print(f"Processing: {file_path}")
                        self._process_article_file(file_path)
        else:
            # Process only the specified files
            for file_path in specific_files:
                if os.path.isfile(file_path) and file_path.endswith(('.html', '.mdx', '.md')):
                    print(f"Processing specified file: {file_path}")
                    self._process_article_file(file_path)
                    
        print(f"\nTotal articles loaded: {len(self.articles)}")
    
    def _process_article_file(self, file_path):
        """Process a single article file and add it to the articles dictionary."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                if file_path.endswith('.html'):
                    title, extracted_content = self.extract_content(content)
                else:  # MDX or MD file
                    # For MDX/MD, the entire content is the content
                    # Extract title from first line if it's a heading
                    lines = content.split('\n')
                    title = ""
                    extracted_content = ""
                    end_frontmatter = 0
                    
                    # Look for title in frontmatter or first heading
                    if lines and lines[0].startswith('---'):
                        # Try to parse frontmatter
                        for i, line in enumerate(lines[1:], 1):
                            if line.strip() == '---':
                                end_frontmatter = i
                                break
                            if ':' in line and not title:
                                key, value = line.split(':', 1)
                                if key.strip().lower() == 'title':
                                    title = value.strip(' "\'')
                    
                    # If no title in frontmatter, use first heading
                    if not title:
                        for line in lines:
                            if line.startswith('# '):
                                title = line[2:].strip()
                                break
                    
                    # Use the rest as content
                    start_idx = end_frontmatter + 1 if end_frontmatter > 0 else 0
                    extracted_content = '\n'.join(lines[start_idx:])
                
                if extracted_content:
                    self.articles[file_path] = {
                        'title': title or os.path.basename(file_path),
                        'content': self.clean_text(extracted_content)
                    }
                    print(f"  ✓ Loaded: {title or os.path.basename(file_path)}")
                else:
                    print(f"  ⚠️  Warning: No content found in {file_path}")
                    
        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {str(e)}")
    
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
    parser = argparse.ArgumentParser(description='Detect duplicate knowledge base articles.')
    parser.add_argument('--directory', type=str, default='knowledge_base',
                       help='Directory containing knowledge base articles')
    parser.add_argument('--threshold', type=float, default=0.8,
                       help='Similarity threshold (0-1)')
    parser.add_argument('--output-format', type=str, choices=['text', 'n8n', 'both'], default='both',
                       help='Output format: text, n8n, or both')
    parser.add_argument('--product-name', type=str, default='',
                       help='Product name for filtering (optional)')
    parser.add_argument('--github-token', type=str, default='',
                       help='GitHub token for posting PR comments (optional)')
    parser.add_argument('--github-event-path', type=str, default='',
                       help='Path to GitHub event JSON file (for PR info)')
    return parser.parse_args()

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

def post_pr_comment(github_token, pr_number, message):
    """Post a comment to a GitHub pull request."""
    import requests
    import os
    
    if not github_token or not pr_number:
        print("GitHub token or PR number not provided, skipping PR comment")
        return False
        
    repo = os.getenv('GITHUB_REPOSITORY')
    if not repo:
        print("GITHUB_REPOSITORY environment variable not set")
        return False
        
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"body": message}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print(f"Successfully posted PR comment to PR #{pr_number}")
        return True
    except Exception as e:
        print(f"Error posting PR comment: {e}")
        return False

def get_pr_number(github_event_path):
    """Extract PR number from GitHub event payload."""
    import json
    
    if not github_event_path or not os.path.exists(github_event_path):
        print(f"GitHub event path not found: {github_event_path}")
        return None
        
    try:
        with open(github_event_path, 'r') as f:
            event = json.load(f)
            # For pull_request events
            if 'pull_request' in event:
                return event['pull_request']['number']
            # For pull_request_target events
            elif 'issue' in event and 'pull_request' in event['issue']:
                return event['issue']['number']
    except Exception as e:
        print(f"Error extracting PR number: {e}")
    
    return None

def format_pr_comment(duplicates, threshold):
    """Format the duplicate detection results as a PR comment."""
    if not duplicates:
        return "No potential duplicate articles found!"
    
    comment = ["## Potential Duplicate Articles Found",
              f"Found {len(duplicates)} potential duplicate{'s' if len(duplicates) > 1 else ''} (similarity ≥ {threshold*100:.0f}%):\n"]
    
    for i, dup in enumerate(duplicates, 1):
        comment.append(f"### {i}. Similarity: {dup['similarity']*100:.1f}%")
        comment.append(f"- **Modified file:** {dup['file1']}")
        comment.append(f"- **Potential duplicate:** {dup['file2']}")
        comment.append(f"- **Titles:** \"{dup['title1']}\" vs \"{dup['title2']}\"")
        comment.append(f"- **Matching content:**\n  ```\n  {dup['snippet1']}\n  ```\n  vs\n  ```\n  {dup['snippet2']}\n  ```\n")
    
    comment.append("\n> This is an automated check. Please review these potential duplicates carefully.")
    return "\n".join(comment)

def main():
    import time
    import json
    import os
    import sys
    
    start_time = time.time()
    args = parse_arguments()
    
    # Get list of modified files
    modified_files = get_modified_files()
    
    # Get PR number if running in GitHub Actions
    pr_number = None
    if args.github_event_path:
        pr_number = get_pr_number(args.github_event_path)
        if pr_number:
            print(f"Detected PR #{pr_number}")
    
    # Prepare empty result structure
    result = {
        "status": "success",
        "execution_details": {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "execution_time_seconds": round(time.time() - start_time, 3)
        },
        "request_details": {
            "product_requested": args.product_name or "All Products",
            "similarity_threshold_used": args.threshold,
            "modified_files_checked": modified_files if modified_files else []
        },
        "results": {
            "articles_processed": 0,
            "potential_duplicates_found": 0,
            "potential_duplicates": []
        }
    }
    
    if not modified_files:
        print("No modified markdown files found in the knowledge base.")
        if args.output_format in ['n8n', 'both']:
            print(json.dumps(result, indent=2))
        return result
    
    print(f"Found {len(modified_files)} modified files to check:")
    for f in modified_files:
        print(f"  - {f}")
    
    try:
        # Create detector instance for the entire knowledge base
        detector = KBDuplicateDetector('knowledge_base', similarity_threshold=args.threshold)
        
        # Process all articles in the knowledge base
        print("Loading all articles from the knowledge base...")
        detector.load_articles()
        print(f"Loaded {len(detector.articles)} articles")
        
        if not detector.articles:
            error_msg = "No articles found in the knowledge base"
            print(error_msg)
            result.update({
                "status": "error",
                "message": error_msg,
                "results": {
                    "articles_processed": 0,
                    "potential_duplicates_found": 0,
                    "potential_duplicates": []
                }
            })
            if args.output_format in ['n8n', 'both']:
                print("\n" + json.dumps(result, indent=2))
            return result
        
        # Update articles processed count
        result['results']['articles_processed'] = len(detector.articles)
        
        # Calculate similarities
        print("Calculating similarities...")
        detector.calculate_similarity()
        
        # Find duplicates for modified files
        print("Checking for duplicates against the entire knowledge base...")
        duplicates = detector.find_duplicates(modified_files=modified_files)
        
        # Update result with duplicates
        result['results'].update({
            'potential_duplicates_found': len(duplicates),
            'potential_duplicates': duplicates
        })
        
        # Update status based on findings
        if duplicates:
            result['status'] = 'warning'
            result['message'] = f'Found {len(duplicates)} potential duplicate(s)'
        else:
            result['message'] = 'No potential duplicates found'
        
        # Update execution time
        result['execution_details']['execution_time_seconds'] = round(time.time() - start_time, 3)
        
        # Generate PR comment if running in GitHub Actions
        if os.getenv('GITHUB_ACTIONS') == 'true' and args.github_token and pr_number:
            comment = format_pr_comment(duplicates, args.threshold)
            post_pr_comment(args.github_token, pr_number, comment)
        
        # Add PR information to the result if available
        if pr_number:
            result['pull_request'] = {
                'number': pr_number,
                'html_url': f"https://github.com/{os.getenv('GITHUB_REPOSITORY', '')}/pull/{pr_number}",
                'head_ref': os.getenv('GITHUB_HEAD_REF', ''),
                'base_ref': os.getenv('GITHUB_BASE_REF', '')
            }
        
        # Save report if needed
        if args.output_format in ['n8n', 'both']:
            # Create reports directory if it doesn't exist
            reports_dir = os.path.join('reports', 'pull_request_qa')
            os.makedirs(reports_dir, exist_ok=True)
            
            # Generate filename with PR info if available
            pr_prefix = f"pr{pr_number}_" if pr_number else ""
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            report_filename = f"{pr_prefix}qa_{timestamp}.json"
            report_path = os.path.join(reports_dir, report_filename)
            
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
            print(f"Report saved to {report_path}")
        
        # Print output in requested format
        if args.output_format == 'text' or args.output_format == 'both':
            if duplicates:
                print(f"\nFound {len(duplicates)} potential duplicate{'s' if len(duplicates) > 1 else ''}:")
                for i, dup in enumerate(duplicates, 1):
                    print(f"\n{i}. Similarity: {dup['similarity']*100:.1f}%")
                    print(f"   File 1: {dup['file1']}")
                    print(f"   File 2: {dup['file2']}")
                    print(f"   Title 1: {dup['title1']}")
                    print(f"   Title 2: {dup['title2']}")
            else:
                print("No potential duplicates found.")
        
        if args.output_format in ['n8n', 'both']:
            print("\n" + json.dumps(result, indent=2))
        
        return result
        
    except Exception as e:
        error_msg = f"An error occurred: {str(e)}"
        print(error_msg)
        result.update({
            "status": "error",
            "message": error_msg,
            "execution_details": {
                "execution_time_seconds": round(time.time() - start_time, 3)
            }
        })
        if args.output_format in ['n8n', 'both']:
            print("\n" + json.dumps(result, indent=2))
        return result

if __name__ == "__main__":
    main()