import os
import re
import html2text
from pathlib import Path

def clean_html_content(html_content):
    """Clean up HTML content before conversion"""
    # Remove script and style elements
    html_content = re.sub(r'<script.*?</script>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<style.*?</style>', '', html_content, flags=re.DOTALL)
    # Remove other unwanted elements
    html_content = re.sub(r'<!--.*?-->', '', html_content, flags=re.DOTALL)
    
    # Replace HTML entities for dashes
    html_content = html_content.replace('&ndash;', '–')
    html_content = html_content.replace('&mdash;', '—')
    html_content = html_content.replace('&nbsp;', ' ')
    
    # Fix headers with bold text that have newlines
    html_content = re.sub(r'(#+)\s*\*\*([^\n]+?)\*\*\s*\n+\s*\*\*', r'\1 **\2**', html_content)
    
    return html_content

def convert_html_to_markdown(html_file, output_file):
    """Convert a single HTML file to Markdown"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Clean HTML content
        html_content = clean_html_content(html_content)
        
        # Configure html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_tables = False
        h.body_width = 0  # Don't wrap lines
        
        # Convert to markdown
        markdown = h.handle(html_content)
        
        # Clean up markdown
        markdown = normalize_newlines(markdown)
        markdown = markdown.strip()
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)
            
        return True, None
    except Exception as e:
        return False, str(e)

def process_directory(input_dir, output_dir, max_files_per_folder=5):
    """Process HTML files in the input directory and save to output directory
    
    Args:
        input_dir: Directory containing HTML files
        output_dir: Directory to save markdown files
        max_files_per_folder: Maximum number of files to process per product folder
    """
    success_count = 0
    error_count = 0
    errors = []
    
    # Get list of product folders
    product_folders = [f for f in os.listdir(input_dir) 
                      if os.path.isdir(os.path.join(input_dir, f))]
    
    for product in product_folders:
        product_path = os.path.join(input_dir, product)
        print(f"\nProcessing product: {product}")
        
        # Reset counter for each product folder
        processed_in_folder = 0
        
        # Process HTML files in the product folder
        for root, _, files in os.walk(product_path):
            for file in files:
                if file.lower().endswith('.html') and processed_in_folder < max_files_per_folder:
                    input_file = os.path.join(root, file)
                    # Calculate relative path for output
                    rel_path = os.path.relpath(root, input_dir)
                    output_path = os.path.join(output_dir, rel_path)
                    os.makedirs(output_path, exist_ok=True)
                    output_file = os.path.join(output_path, os.path.splitext(file)[0] + '.md')
                    
                    print(f"  Converting: {file}")
                    success, error = convert_html_to_markdown(input_file, output_file)
                    
                    if success:
                        success_count += 1
                        processed_in_folder += 1
                    else:
                        error_count += 1
                        errors.append(f"Error processing {input_file}: {error}")
            
            # Break after processing the first level of the directory
            break
    
    # Print summary
    print("\nConversion complete!")
    print(f"Successfully converted: {success_count} files")
    print(f"Errors: {error_count} files")
    
    if errors:
        print("\nErrors encountered:")
        for error in errors:
            print(f"- {error}")

if __name__ == "__main__":
    # Set up paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_dir = os.path.join(base_dir, 'kb-html')
    output_dir = os.path.join(base_dir, 'kb-mdx')
    
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    
    # Process files
    process_directory(input_dir, output_dir)
