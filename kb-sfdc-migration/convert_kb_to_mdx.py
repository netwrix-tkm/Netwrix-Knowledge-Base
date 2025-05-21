import pandas as pd
import os
import html
import html2markdown
import frontmatter
from slugify import slugify
from datetime import datetime
import re

# Configuration
INPUT_CSV = "kb_all.csv"
OUTPUT_DIR = "./kb-markdown"

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

def clean_html(html_content):
    """Clean up HTML content before conversion"""
    if pd.isna(html_content):
        return ""
    
    # Remove script and style tags completely
    html_content = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', html_content, flags=re.IGNORECASE | re.DOTALL)
    html_content = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', html_content, flags=re.IGNORECASE | re.DOTALL)
    
    # Handle headers (h1-h6)
    for i in range(1, 7):
        html_content = re.sub(
            f'<h{i}[^>]*>(.*?)</h{i}>',
            lambda m: f'\n\n{"#" * i} {m.group(1).strip()}\n\n',
            html_content,
            flags=re.IGNORECASE | re.DOTALL
        )
    
    # Handle code blocks - preserve them before general HTML processing
    def process_code_block(match):
        # Get the full match and the inner content
        full_match = match.group(0)
        
        # Check if it's a <pre> with <code> inside
        if '<code' in full_match.lower() and '</code>' in full_match.lower():
            # Extract just the code content
            code = re.search(r'<code[^>]*>(.*?)<\/code>', full_match, flags=re.DOTALL | re.IGNORECASE)
            if code:
                code_content = code.group(1).strip()
                code_content = html.unescape(code_content)
                code_content = re.sub(r'<[^>]+>', '', code_content)
                return f'\n```\n{code_content}\n```\n'
        
        # Handle standalone <pre> tags
        if full_match.lower().startswith('<pre'):
            pre_content = re.sub(r'<pre[^>]*>', '', full_match, flags=re.IGNORECASE)
            pre_content = re.sub(r'<\/pre>', '', pre_content, flags=re.IGNORECASE)
            pre_content = html.unescape(pre_content).strip()
            pre_content = re.sub(r'<[^>]+>', '', pre_content)
            # Only wrap in code blocks if the content looks like code (has line breaks)
            if '\n' in pre_content:
                return f'\n```\n{pre_content}\n```\n'
            return f'\n{pre_content}\n'
            
        # Default case - just return the content without code markers
        content = re.sub(r'<[^>]+>', '', full_match)
        return f'\n{html.unescape(content).strip()}\n'
    
    html_content = re.sub(
        r'<pre[^>]*>\s*<code[^>]*>(.*?)</code>\s*</pre>',
        process_code_block,
        html_content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    # Handle <br> tags
    html_content = re.sub(r'<br\s*/?>', '  \n', html_content, flags=re.IGNORECASE)
    
    # Clean up any remaining HTML tags but keep their content
    # But first, handle any remaining <pre> tags that might have been missed
    def handle_remaining_pre(match):
        pre_content = match.group(1).strip()
        if pre_content and '```' not in pre_content:  # Avoid double-wrapping
            return f'\n```\n{pre_content}\n```\n'
        return f'\n{pre_content}\n'
    
    html_content = re.sub(r'<pre[^>]*>(.*?)</pre>', handle_remaining_pre, html_content, flags=re.IGNORECASE | re.DOTALL)
    
    # Now remove any remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)
    
    # Clean up multiple newlines and spaces
    html_content = re.sub(r'\n{3,}', '\n\n', html_content)
    html_content = re.sub(r' +', ' ', html_content)
    
    # Replace <div> with newlines, but be careful with lists inside divs
    def process_divs(html):
        # First, protect list items inside divs
        def protect_list(match):
            content = match.group(1)
            # If the div contains a list, keep it as is
            if '<li>' in content.lower() or '<ul>' in content.lower() or '<ol>' in content.lower():
                return content
            # Otherwise, replace div with newlines
            return f'\n{content}\n'
        
        # Process divs that might contain lists
        html = re.sub(
            r'<div[^>]*>(.*?)</div>',
            protect_list,
            html,
            flags=re.IGNORECASE | re.DOTALL
        )
        
        # Handle any remaining divs
        html = re.sub(r'<div[^>]*>', '\n', html, flags=re.IGNORECASE)
        html = html.replace('</div>', '\n')
        return html
    
    html_content = process_divs(html_content)
    
    # Replace <p> with double newlines
    html_content = re.sub(r'<p[^>]*>', '\n\n', html_content, flags=re.IGNORECASE)
    html_content = html_content.replace('</p>', '\n\n')
    
    # Handle lists - first process list items to avoid empty bullets
    def process_list_item(match):
        item_content = match.group(1).strip()
        # Skip empty list items
        if not item_content or item_content.isspace():
            return '\n'
        
        # Clean up the item content
        item_content = re.sub(r'<[^>]+>', '', item_content)  # Remove any remaining HTML tags
        item_content = re.sub(r'\s+', ' ', item_content).strip()
        
        # Check if this is a nested list item by looking at the parent context
        parent_tag = ''
        if match.lastindex > 1:  # If we have a parent tag group
            parent_tag = match.group(2).lower() if match.group(2) else ''
        
        # Add proper indentation for nested lists
        indent = '    ' if parent_tag in ('ol', 'ul') else ''
        
        # Add proper line breaks around list items
        return f'\n{indent}* {item_content}\n'
    
    # First, handle nested lists with proper context
    def process_nested_lists(html):
        # Process lists with their items
        def process_whole_list(match):
            list_type = match.group(1).lower()
            list_items = match.group(2)
            
            # Split list items that contain multiple sentences without proper list markup
            list_items = re.sub(
                r'([.!?])\s*([A-Z])', 
                lambda m: f'{m.group(1)}\n* {m.group(2).lower()}', 
                list_items
            )
            
            # Process each list item with proper context
            list_items = re.sub(
                r'<li[^>]*>(.*?)</li>',
                lambda m: f'\n* {m.group(1).strip()}\n',
                list_items,
                flags=re.IGNORECASE | re.DOTALL
            )
            
            # Add proper spacing around list items
            list_items = re.sub(r'\n\*\s*\n', '\n', list_items)  # Remove empty list items
            return f'\n{list_items}\n'
        
        # Handle both ordered and unordered lists
        html = re.sub(
            r'<(ul|ol)[^>]*>(.*?)</\1>',
            process_whole_list,
            html,
            flags=re.IGNORECASE | re.DOTALL
        )
        
        # Handle instructions that should be lists but aren't properly marked up
        # Look for patterns like "1. Text. 2. Text" or "- Text. - Text"
        html = re.sub(
            r'(\d+\.\s*[^\n.]+)(?=\s+\d+\.|$)',
            lambda m: f'\n* {m.group(1).strip()}\n',
            html
        )
        
        # Handle dash-separated items
        html = re.sub(
            r'([^\n])(\s*-\s*)([^\n]+)(?=\s+-|$)',
            lambda m: f'{m.group(1)}\n* {m.group(3).strip()}\n',
            html
        )
        
        return html
    
    # Process nested lists first
    html_content = process_nested_lists(html_content)
    
    # Then handle any remaining standalone list items
    html_content = re.sub(
        r'<li[^>]*>(.*?)</li>',
        lambda m: f'\n* {m.group(1).strip()}\n',
        html_content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    # Clean up list containers
    html_content = re.sub(r'<ul[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<ol[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</[ou]l>', '\n', html_content, flags=re.IGNORECASE)
    
    # Clean up list formatting and spacing
    html_content = re.sub(r'\n\*\s*\n', '\n\n', html_content)  # Remove empty list items
    
    # Fix instructions that should be on separate lines
    html_content = re.sub(
        r'([.!?])\s*([A-Z])', 
        lambda m: f'{m.group(1)}\n\n{m.group(2)}', 
        html_content
    )
    
    # Fix list items that run together
    html_content = re.sub(
        r'(\n\* [^\n]+?)\.\s*([A-Z])', 
        lambda m: f'{m.group(1)}.\n\n{m.group(2).lower()}', 
        html_content
    )
    
    # Ensure proper spacing around lists
    html_content = re.sub(r'([^\n])(\n\* )', r'\1\n\2', html_content)  # Add newline before list if missing
    html_content = re.sub(r'(\n\* [^\n]*)\n([^\n*])', r'\1\n\n\2', html_content)  # Add newline after list if missing
    
    # Fix multiple consecutive list items
    html_content = re.sub(r'(\n\* [^\n]*)(\n\* )', r'\1\2', html_content)
    
    # Fix Windows/macOS specific instructions
    html_content = re.sub(
        r'(For (?:Windows|macOS) operating systems:)\s*([^\n]+)',
        lambda m: f'### {m.group(1)}\n\n{m.group(2).strip()}',
        html_content,
        flags=re.IGNORECASE
    )
    
    # Fix instructions that should be lists
    for pattern in [
        (r'(In the [^:]+:)([^\n]+)', r'\1\n\n\2'),  # Instructions with colons
        (r'(Click|Select|Verify|Ensure|Attempt to|Navigate to)([^\n]+?)(?=\s+[A-Z][a-z]|$)', r'* \1\2\n'),  # Action items
    ]:
        html_content = re.sub(pattern[0], pattern[1], html_content, flags=re.IGNORECASE)
    
    # Handle <strong> tags (convert to **bold**)
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.IGNORECASE | re.DOTALL)
    
    # Handle <a> tags
    def process_links(html):
        # First, handle links with both href and text
        html = re.sub(
            r'<a\s+(?:[^>]*?\s+)?href=(["\'])(.*?)\1[^>]*>(.*?)</a>',
            lambda m: f'[{m.group(3).strip()}]({m.group(2).strip()})',
            html,
            flags=re.IGNORECASE | re.DOTALL
        )
        
        # Then handle any remaining links that might have been missed
        html = re.sub(
            r'<a\s+[^>]*?href=(["\'])(.*?)\1[^>]*>(.*?)</a>',
            lambda m: f'[{m.group(3).strip()}]({m.group(2).strip()})',
            html,
            flags=re.IGNORECASE | re.DOTALL
        )
        return html
    
    html_content = process_links(html_content)
    
    return html_content.strip()

def convert_html_to_markdown(html_content):
    """Convert HTML to markdown using html2markdown with custom handling"""
    if not html_content or pd.isna(html_content):
        return ""
    
    try:
        # Clean HTML first (removes scripts, styles, preserves code blocks)
        clean_content = clean_html(html_content)
        
        # Convert to markdown using html2markdown
        markdown = html2markdown.convert(clean_content)
        
        # Clean up any remaining HTML entities
        markdown = html.unescape(markdown)
        
        # Clean up multiple newlines (no more than 2 consecutive)
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        
        return markdown.strip()
    except Exception as e:
        print(f"Error converting HTML to markdown: {e}")
        # Return original content if conversion fails
        return str(html_content)

def create_slug(title, id_value):
    """Create a URL-friendly slug from title with ID as fallback"""
    if pd.isna(title) or not str(title).strip():
        return f"kb-{id_value}"
    
    # Create slug from title and append ID for uniqueness
    slug = slugify(str(title))
    if not slug:
        return f"kb-{id_value}"
    return f"{slug}-{id_value}"

def detect_encoding(file_path):
    """Detect the file encoding"""
    try:
        import chardet
        with open(file_path, 'rb') as f:
            rawdata = f.read(10000)  # Read first 10KB to guess encoding
        result = chardet.detect(rawdata)
        return result.get('encoding', 'utf-8')
    except Exception as e:
        print(f"Warning: Could not detect encoding, falling back to 'utf-8'. Error: {e}")
        return 'utf-8'

def has_img_tag(content):
    """Check if content contains <img> tags"""
    if pd.isna(content):
        return False
    return '<img' in str(content).lower()

def process_csv(test_mode=True, max_articles=10):
    """Process the CSV file and generate MDX files
    
    Args:
        test_mode (bool): If True, only process a few articles for testing
        max_articles (int): Maximum number of articles to process in test mode
    """
    print(f"Starting to process CSV file: {INPUT_CSV}")
    if test_mode:
        print(f"TEST MODE: Only processing first {max_articles} articles with images")
    
    try:
        # Detect file encoding
        encoding = detect_encoding(INPUT_CSV)
        print(f"Detected encoding: {encoding}")
        
        # Try reading with detected encoding, fall back to latin1 if that fails
        try:
            df = pd.read_csv(INPUT_CSV, low_memory=False, encoding=encoding)
        except UnicodeDecodeError:
            print("Falling back to 'latin1' encoding...")
            df = pd.read_csv(INPUT_CSV, low_memory=False, encoding='latin1')
        
        # Clean up any leading/trailing spaces in column names
        df.columns = df.columns.str.strip()
        print(f"Found columns: {', '.join(df.columns[:10])}...")  # Show first 10 columns
        total_rows = len(df)
        print(f"Found {total_rows} articles to process")
        
        # Filter for articles with <img> tags in Content__c
        df['has_img'] = df['Content__c'].apply(has_img_tag)
        img_articles = df[df['has_img']].copy()
        
        if test_mode:
            img_articles = img_articles.head(max_articles)
        
        total_articles = len(img_articles)
        print(f"Found {total_articles} articles with images")
        
        if total_articles == 0:
            print("No articles with images found in the CSV file")
            return
        
        # Process each row with images
        success_count = 0
        error_count = 0
        
        for index, row in img_articles.iterrows():
            try:
                # Get required fields
                article_id = str(row.get('Id', '')).strip()
                if not article_id:
                    print(f"Skipping row {index}: Missing ID")
                    error_count += 1
                    continue
                
                title = row.get('Title', '').strip()
                if not title:
                    title = f"Untitled-{article_id}"
                
                # Use ArticleNumber for filename, fallback to ID if not available
                article_number = str(row.get('ArticleNumber', '')).strip()
                if not article_number or article_number.lower() == 'nan':
                    article_number = f"article-{article_id}"
                filename = f"{article_number}.mdx"
                filepath = os.path.join(OUTPUT_DIR, filename)
                
                # Prepare frontmatter with more metadata
                frontmatter_data = {
                    'title': title,
                    'id': article_id,
                    'article_number': article_number,
                    'date': row.get('CreatedDate', datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')),
                    'last_modified': row.get('LastModifiedDate', datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')),
                    'draft': False,
                    'has_images': True
                }
                
                # Add all other columns as frontmatter (except content)
                for col in df.columns:
                    if col not in ['Content__c', 'Title', 'Id'] and not pd.isna(row[col]):
                        frontmatter_data[col.lower()] = row[col]
                
                # Convert content to markdown
                html_content = row.get('Content__c', '')
                markdown_content = convert_html_to_markdown(html_content)
                
                # Create the MDX file with frontmatter
                post = frontmatter.Post(markdown_content, **frontmatter_data)
                
                # Write to file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(frontmatter.dumps(post))
                
                success_count += 1
                if test_mode or success_count % 100 == 0:
                    print(f"Processed {success_count}/{total_rows} articles...")
                
            except Exception as e:
                print(f"Error processing article {index} (ID: {article_id}): {str(e)}")
                error_count += 1
        
        print(f"\nProcessing complete!")
        print(f"Successfully processed: {success_count} articles")
        print(f"Errors: {error_count} articles")
        
    except Exception as e:
        import traceback
        print(f"Error processing CSV file: {str(e)}")
        print("\nDetailed error:")
        traceback.print_exc()
        
        # Try to provide more helpful error messages
        if 'utf-8' in str(e).lower():
            print("\nTry specifying a different encoding when reading the CSV file.")
            print("Common encodings to try: 'latin1', 'cp1252', 'iso-8859-1'")
            print("Example: df = pd.read_csv(INPUT_CSV, encoding='latin1')")

def main():
    # Run in test mode to process 10 articles
    print("Running in test mode with 10 articles...")
    process_csv(test_mode=True, max_articles=10)
    
    # After testing, uncomment to process all articles
    # process_csv(test_mode=False)

if __name__ == "__main__":
    main()
