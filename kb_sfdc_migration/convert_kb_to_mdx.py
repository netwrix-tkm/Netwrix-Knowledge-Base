print("=== Script started successfully ===")

import pandas as pd
import os
import html
import html2markdown
import frontmatter
from slugify import slugify
from datetime import datetime
import re
import sys
from collections import defaultdict
from pathlib import Path

# Configuration
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_CSV = os.path.join(SCRIPT_DIR, "kb_all.csv")
CATEGORIES_CSV = os.path.join(SCRIPT_DIR, "kb_data_categories.csv")
HTML_DIR = os.path.join(SCRIPT_DIR, "kb-html")
MARKDOWN_DIR = os.path.join(SCRIPT_DIR, "kb-markdown")

# Mapping of old product names to new folder names
PRODUCT_MAPPING = {
    'access_info_center': 'Access Information Center', 
    'activity_monitor': 'Activity Monitor',
    'onesecure': '1Secure',
    'auditor': 'Auditor',
    'change_tracker': 'Change Tracker',
    'data_classification': 'Data Classification',
    'endpoint_protector': 'Endpoint Protector',
    'groupid': 'Directory Manager',
    'log_tracker': 'Log Tracker',
    'password_policy_enforcer': 'Password Policy Enforcer',
    'password_reset_manager': 'Password Reset',
    'password_secure': 'Password Secure',
    'policypak': 'Endpoint Policy Manager',
    'privilege_secure_endpoints': 'Endpoint Privilege Manager',
    'privilege_secure': 'Privilege Secure for Access Management',
    'privilege_secure_discovery': 'Privilege Secure for Discovery',
    'recovery_ad': 'Recovery for Active Directory',
    'enterprise_auditor': 'Access Analyzer',
    'threat_manager': 'Threat Manager',
    'threat_prevention': 'Threat Prevention',
    'strongpoint_netsuite': 'Platform Governance for NetSuite',
    'strongpoint_salesforce': 'Platform Governance for Salesforce',
    'usercube': 'Identity Manager',
    'vulnerability_tracker': 'Vulnerability Tracker'
}

# Create output directories if they don't exist
os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(MARKDOWN_DIR, exist_ok=True)

# Create 'Other' directory for articles without product categories in both HTML and Markdown
os.makedirs(os.path.join(HTML_DIR, 'Other'), exist_ok=True)
os.makedirs(os.path.join(MARKDOWN_DIR, 'Other'), exist_ok=True)

def get_output_dir(article, output_base_dir):
    """
    Determine the output directory based on the article's product categories.
    This is a simplified version that just returns the base directory,
    as we now handle the directory creation in the main processing loop.
    """
    return output_base_dir

def clean_html(html_content):
    """Clean up HTML content before conversion"""
    if pd.isna(html_content):
        return ""
    
    # Convert to string in case it's not already
    html_content = str(html_content)
    
    # Replace HTML entities for dashes and other special characters
    html_content = html_content.replace('&ndash;', '–')
    html_content = html_content.replace('&mdash;', '—')
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&quot;', '"')
    html_content = html_content.replace('&amp;', '&')
    
    # Remove script and style tags completely
    html_content = re.sub(r'<script\b[^<]*(?:(?<!<\/script>)<[^<]*)*<\/script>', '', html_content, flags=re.IGNORECASE | re.DOTALL)
    html_content = re.sub(r'<style\b[^<]*(?:(?<!<\/style>)<[^<]*)*<\/style>', '', html_content, flags=re.IGNORECASE | re.DOTALL)
    
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
        
        # Handle links more robustly
        def process_links(html):
            # Process <a> tags to ensure they're properly converted to markdown
            def replace_link(match):
                text = match.group(1) or match.group(2) or ''
                href = match.group(3) or ''
                # Clean up any newlines in the link text
                text = re.sub(r'\s+', ' ', text).strip()
                # Clean up the URL
                href = re.sub(r'\s+', '', href)
                return f'[{text}]({href})'
            
            # Handle both <a> tags and plain URLs
            html = re.sub(
                r'<a\s+(?:[^>]*?\s+)?href=["\']([^"\']+)["\'][^>]*>(.*?)</a>',
                replace_link,
                html,
                flags=re.IGNORECASE | re.DOTALL
            )
            
            # Convert remaining plain URLs to markdown links
            html = re.sub(
                r'(?<!\[)(https?://[^\s\n<>\]"\']+)',
                lambda m: f'<{m.group(1)}>',
                html
            )
            return html
        
        # Process links before conversion
        clean_content = process_links(clean_content)
        
        # Convert to markdown using html2markdown
        markdown = html2markdown.convert(clean_content)
        
        # Clean up any remaining HTML entities
        markdown = html.unescape(markdown)
        
        # Fix common markdown formatting issues
        markdown = re.sub(r'\*\s+\*', ' ', markdown)  # Remove empty bold/italic markers
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)  # Limit consecutive newlines
        markdown = re.sub(r'\s+\n', '\n', markdown)  # Remove trailing whitespace
        
        # Fix list formatting
        markdown = re.sub(r'\n(\s*[-*+])\s+\n', '\n\1 ', markdown)
        
        # Ensure proper spacing around headings
        markdown = re.sub(r'\n(#{1,6})\s*', '\n\1 ', markdown)
        
        return markdown.strip()
    except Exception as e:
        print(f"Error converting HTML to markdown: {e}")
        import traceback
        traceback.print_exc()
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

def load_categories(categories_path):
    """Load and categorize the data from kb_data_categories.csv"""
    categories = defaultdict(lambda: {
        'visibility': [],
        'content_type': [],
        'former_brand': [],
        'product': []
    })
    
    if not os.path.exists(categories_path):
        print(f"Warning: Categories file not found at {categories_path}")
        return categories
    
    try:
        # Try to detect encoding
        def detect_encoding(file_path):
            try:
                import chardet
                with open(file_path, 'rb') as f:
                    result = chardet.detect(f.read())
                    return result['encoding'] or 'latin1'
            except ImportError:
                return 'latin1'
        
        encoding = detect_encoding(categories_path)
        df_categories = pd.read_csv(categories_path, encoding=encoding)
        
        # Process each category
        for _, row in df_categories.iterrows():
            parent_id = row.get('ParentId', '').strip()
            data_category = row.get('DataCategoryName', '').strip()
            
            if not parent_id or not data_category:
                continue
            
            # Categorize the tag
            if data_category.endswith('_v'):
                categories[parent_id]['visibility'].append(data_category)
            elif data_category.startswith('ct_'):
                categories[parent_id]['content_type'].append(data_category)
            elif data_category.startswith('f_'):
                categories[parent_id]['former_brand'].append(data_category)
            elif data_category in PRODUCT_MAPPING:
                # Only include product categories that are in our mapping
                categories[parent_id]['product'].append(data_category)
                
    except Exception as e:
        print(f"Error loading categories: {str(e)}")
    
    return categories

def save_html_content(content, output_path):
    """Save HTML content to a file"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error saving HTML to {output_path}: {str(e)}")
        return False

def process_csv(test_mode=True, max_articles_per_product=5):
    """Process the CSV file and generate HTML and MDX files
    
    Args:
        test_mode (bool): If True, only process a few articles for testing
        max_articles_per_product (int): Maximum number of articles to process per product
    """
    print("Debug: Entering process_csv function")
    print(f"Starting to process CSV file: {INPUT_CSV}")
    print(f"Loading categories from: {CATEGORIES_CSV}")
    print(f"Input CSV exists: {os.path.exists(INPUT_CSV)}")
    
    # Load categories
    categories = load_categories(CATEGORIES_CSV)
    
    if test_mode:
        print(f"TEST MODE: Processing up to {max_articles_per_product} articles per product")
        # Try different encodings to read the CSV file
        import pandas as pd  # Ensure pandas is imported
        encodings = ['utf-8-sig', 'utf-8', 'latin1', 'cp1252']
        df = None
        
        for encoding in encodings:
            try:
                print(f"Trying encoding: {encoding}")
                df = pd.read_csv(INPUT_CSV, low_memory=False, encoding=encoding, on_bad_lines='warn')
                if not df.empty:
                    print(f"Successfully read CSV with {encoding} encoding")
                    print(f"CSV shape: {df.shape} (rows x columns)")
                    print(f"Columns: {df.columns.tolist()}")
                    break
            except Exception as e:
                print(f"Failed with {encoding}: {str(e)}")
                continue
                
        if df is None or df.empty:
            raise ValueError("Failed to read CSV file with any encoding. Please check the file format.")
    
    if df is None:
        raise ValueError("Failed to read the CSV file with any of the attempted encodings")
    
    try:
        # Clean up any leading/trailing spaces in column names
        df.columns = df.columns.str.strip()
        print(f"Found columns: {', '.join(df.columns[:10])}...")  # Show first 10 columns
        total_rows = len(df)
        print(f"Found {total_rows} articles to process")
        
        # Process articles with their categories
        # Initialize product counts and processed articles list
        product_counts = {}
        processed_articles = []  # Initialize the list to store processed articles
        
        if test_mode:
            # Initialize all known products with count 0
            for product in PRODUCT_MAPPING.values():
                product_counts[product] = 0
            product_counts['Other'] = 0  # For articles with no valid product
        
        # Get unique articles (filter for latest version if needed)
        if 'IsLatestVersion' in df.columns:
            df = df[df['IsLatestVersion'] == True].copy()
        
        # Process each article
        for idx, row in df.iterrows():
            if idx % 100 == 0:
                print(f"Processing article {idx + 1}/{len(df)}")
            
            article_id = str(row.get('Id', '')).strip()
            if not article_id:
                print(f"Skipping row {idx}: Missing article ID")
                continue
            
            # Get categories for this article
            article_cats = categories.get(article_id, {})
            products = article_cats.get('product', [])
            
            # Print some debug info for the first few articles
            if idx < 5:
                print(f"\nProcessing article {idx} (ID: {article_id})")
                print(f"  Title: {row.get('Title', 'No title')}")
                print(f"  Products: {products}")
                print(f"  Categories: {article_cats}")
            
            # If no products found, assign to 'Other' category
            if not products:
                if test_mode:
                    print(f"No product categories found for article ID: {article_id}, assigning to 'Other'")
                products = ['Other']
            
            # Find the first valid product for this article
            primary_product = 'Other'
            for product in products:
                if product in PRODUCT_MAPPING:
                    primary_product = PRODUCT_MAPPING[product]
                    break
            
            # For test mode, check if we've reached the limit for this product
            if test_mode:
                if product_counts.get(primary_product, 0) >= max_articles_per_product:
                    if idx < 5:  # Only print for first few articles to avoid too much output
                        print(f"  Skipping - reached limit for product: {primary_product}")
                    continue
                
                # Update the count for this product
                product_counts[primary_product] = product_counts.get(primary_product, 0) + 1
                print(f"  Adding article to product: {primary_product} (count: {product_counts[primary_product]})")
                
                # Check if we've processed enough articles for all products
                all_products_done = all(count >= max_articles_per_product 
                                    for product, count in product_counts.items() 
                                    if product != 'Other' or len(products) == 0)  # Only check 'Other' if it was explicitly assigned
                
                if all_products_done and idx > 5:  # Ensure we process at least a few articles
                    print("Reached maximum articles for all products in test mode")
                    break
                
                if all_products_done:
                    print("\nReached maximum articles per product limit for all products.")
                    break
            
            # Add categories to the row
            row_dict = row.to_dict()
            row_dict.update({
                'categories': article_cats,
                'products': products
            })
            processed_articles.append(row_dict)
        
        print(f"Found {len(processed_articles)} articles to process")
        
        total_articles = len(processed_articles)
        print(f"Found {total_articles} total articles across all products")
        
        # Convert back to DataFrame for easier processing
        df_processed = pd.DataFrame(processed_articles)
        
        if total_articles == 0:
            print("No articles with images found in the CSV file")
            return
        
        # Process each article
        success_count = 0
        error_count = 0
        
        for _, row in df_processed.iterrows():
            try:
                # Get required fields
                article_id = str(row.get('Id', '')).strip()
                if not article_id:
                    print("Skipping article with missing ID")
                    error_count += 1
                    continue
                    
                # Get categories
                categories = row.get('categories', {})
                products = row.get('products', [])
                
                title = row.get('Title', '').strip()
                if not title:
                    title = f"Untitled-{article_id}"
                
                # Get product categories for this article
                product_tags = row.get('products', [])
                
                # Get the primary product for directory structure
                primary_product = None
                if product_tags:
                    # Use the first product tag that exists in our mapping
                    for tag in product_tags:
                        if tag in PRODUCT_MAPPING:
                            primary_product = PRODUCT_MAPPING[tag]
                            break
                
                # If no valid product found, use 'Other'
                if not primary_product:
                    primary_product = 'Other'
                
                # Create output directories for both HTML and Markdown
                html_output_dir = os.path.join(HTML_DIR, primary_product)
                md_output_dir = os.path.join(MARKDOWN_DIR, primary_product)
                
                os.makedirs(html_output_dir, exist_ok=True)
                os.makedirs(md_output_dir, exist_ok=True)
                
                # Create a safe filename using the article number
                article_number = str(row.get('ArticleNumber', '')).strip()
                if not article_number or article_number.lower() == 'nan':
                    print(f"Warning: Missing article number for article ID: {article_id}")
                    article_number = f"article_{article_id[:8]}"
                
                # Create the HTML and MDX filenames
                html_filename = f"{article_number}.html"
                mdx_filename = f"{article_number}.mdx"
                
                html_path = os.path.join(html_output_dir, html_filename)
                output_path = os.path.join(md_output_dir, mdx_filename)
                
                # Prepare frontmatter with more metadata
                frontmatter_data = {
                    'title': title,
                    'id': article_id,
                    'article_number': article_number,
                    'date': row.get('CreatedDate', datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')),
                    'last_modified': row.get('LastModifiedDate', datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')),
                    'draft': False,
                    'has_images': has_img_tag(row.get('Content__c', '')),
                    'products': product_tags,  # Include all product tags
                    'visibility': row.get('categories', {}).get('visibility', []),
                    'content_type': row.get('categories', {}).get('content_type', []),
                    'former_brand': row.get('categories', {}).get('former_brand', [])
                }
                
                # Add all other columns as frontmatter (except content)
                for col in df.columns:
                    if col not in ['Content__c', 'Title', 'Id'] and not pd.isna(row[col]):
                        frontmatter_data[col.lower()] = row[col]
                
                # Convert content to markdown
                html_content = row.get('Content__c', '')
                markdown_content = convert_html_to_markdown(html_content)
                error_count += 1
                continue
                
                # Get categories
                categories = row.get('categories', {})
                products = row.get('products', [])
                
                title = row.get('Title', '').strip()
                if not title:
                    title = f"Untitled-{article_id}"
                
                # Get product categories for this article
                product_tags = row.get('products', [])
                
                # Get the primary product for directory structure
                primary_product = None
                if product_tags:
                    # Use the first product tag that exists in our mapping
                    for tag in product_tags:
                        if tag in PRODUCT_MAPPING:
                            primary_product = PRODUCT_MAPPING[tag]
                            break
                
                # If no valid product found, use 'Other'
                if not primary_product:
                    primary_product = 'Other'
                
                # Create output directories for both HTML and Markdown
                html_output_dir = os.path.join(HTML_DIR, primary_product)
                md_output_dir = os.path.join(MARKDOWN_DIR, primary_product)
                
                os.makedirs(html_output_dir, exist_ok=True)
                os.makedirs(md_output_dir, exist_ok=True)
                
                # Create a safe filename using the article number
                article_number = str(row.get('ArticleNumber', '')).strip()
                if not article_number or article_number.lower() == 'nan':
                    print(f"Warning: Missing article number for article ID: {article_id}")
                    article_number = f"article_{article_id[:8]}"
                
                # Create the HTML and MDX filenames
                html_filename = f"{article_number}.html"
                mdx_filename = f"{article_number}.mdx"
                
                html_path = os.path.join(html_output_dir, html_filename)
                output_path = os.path.join(md_output_dir, mdx_filename)
                
                # Prepare frontmatter with more metadata
                frontmatter_data = {
                    'title': title,
                    'id': article_id,
                    'article_number': article_number,
                    'date': row.get('CreatedDate', datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')),
                    'last_modified': row.get('LastModifiedDate', datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')),
                    'draft': False,
                    'has_images': has_img_tag(row.get('Content__c', '')),
                    'products': product_tags,  # Include all product tags
                    'visibility': row.get('categories', {}).get('visibility', []),
                    'content_type': row.get('categories', {}).get('content_type', []),
                    'former_brand': row.get('categories', {}).get('former_brand', [])
                }
                
                # Add all other columns as frontmatter (except content)
                for col in df.columns:
                    if col not in ['Content__c', 'Title', 'Id'] and not pd.isna(row[col]):
                        frontmatter_data[col.lower()] = row[col]
                
                # Convert content to markdown
                html_content = row.get('Content__c', '')
                markdown_content = convert_html_to_markdown(html_content)
                
                # Create the MDX file with frontmatter
                try:
                    # Ensure the output directories exist
                    os.makedirs(os.path.dirname(html_path), exist_ok=True)
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    
                    # Save the HTML content first
                    html_content = str(row.get('Content__c', ''))
                    if html_content and html_content.lower() != 'nan':
                        with open(html_path, 'w', encoding='utf-8') as f:
                            f.write(html_content)
                        print(f"Created HTML: {html_path}")
                    
                    # Convert to markdown and save
                    markdown_content = convert_html_to_markdown(html_content)
                    
                    # Write the MDX file
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(frontmatter.dumps(frontmatter_data) + '\n\n' + markdown_content)
                    print(f"Created MDX: {output_path}")
                    
                    success_count += 1
                    
                except Exception as e:
                    print(f"Error processing article {article_id}: {str(e)}")
                    error_count += 1
                    continue
                
                if test_mode or success_count % 10 == 0:  # Print progress more frequently
                    print(f"Processed {success_count} articles (successful: {success_count}, errors: {error_count})...")
                
            except Exception as e:
                print(f"Error processing article {idx} (ID: {article_id}): {str(e)}")
                error_count += 1
                continue
        
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

def main():
    print("=== Starting conversion process ===")
    print("Debug: Entering main function")
    print(f"Script started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Python version: {sys.version}")
    
    # Get absolute paths to input files
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(script_dir, "kb_all.csv")
    categories_csv = os.path.join(script_dir, "kb_data_categories.csv")
    
    print(f"Current working directory: {os.getcwd()}")
    print(f"Script directory: {script_dir}")
    print(f"Input CSV path: {input_csv}")
    print(f"Categories CSV path: {categories_csv}")
    print(f"HTML output directory: {os.path.abspath(HTML_DIR)}")
    print(f"Markdown output directory: {os.path.abspath(MARKDOWN_DIR)}")
    
    # Check if input files exist
    input_exists = os.path.exists(input_csv)
    categories_exist = os.path.exists(categories_csv)
    
    print(f"\nFile Status:")
    print(f"- Input CSV exists: {input_exists}")
    print(f"- Categories CSV exists: {categories_exist}")
    
    if not input_exists:
        print(f"\nError: Input CSV file not found at {input_csv}")
        # List files in the script directory to help with debugging
        print("\nFiles in script directory:")
        try:
            for f in os.listdir(script_dir):
                if f.endswith('.csv'):
                    print(f"  - {f}")
        except Exception as e:
            print(f"  Could not list directory contents: {e}")
        return
    
    # Update global variables with absolute paths
    global INPUT_CSV, CATEGORIES_CSV
    INPUT_CSV = input_csv
    CATEGORIES_CSV = categories_csv
    
    try:
        print("Debug: Creating output directories")
        # Create output directories if they don't exist
        os.makedirs(HTML_DIR, exist_ok=True)
        os.makedirs(MARKDOWN_DIR, exist_ok=True)
        print(f"Debug: Output directories created - HTML: {os.path.abspath(HTML_DIR)}, Markdown: {os.path.abspath(MARKDOWN_DIR)}")
        
        # Load categories (even if the file doesn't exist, the function will handle it)
        print("\nLoading categories...")
        categories = load_categories(CATEGORIES_CSV)
        print(f"Loaded categories for {len(categories)} articles")
        
        # Print some sample categories for debugging
        if categories:
            print("\nSample categories (first 5):")
            for i, (art_id, cats) in enumerate(list(categories.items())[:5]):
                print(f"  {art_id}: {cats}")
        
        print("\nRunning in test mode with 5 articles per product...")
        print("Debug: About to call process_csv")
        process_csv(test_mode=True, max_articles_per_product=5)
        print("Debug: Returned from process_csv")
        
        print("\nScript completed successfully!")
        
    except Exception as e:
        print(f"\nError in main execution: {str(e)}")
        import traceback
        traceback.print_exc()
    
    # After testing, uncomment to process all articles
    # process_csv(test_mode=False)

if __name__ == "__main__":
    main()
