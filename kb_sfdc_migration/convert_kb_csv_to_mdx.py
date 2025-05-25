import os
import pandas as pd
from pathlib import Path
import html
import re
from collections import defaultdict
import frontmatter
from slugify import slugify
from datetime import datetime
import html2markdown

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)  # Go up one level to the root directory
INPUT_CSV = os.path.join(SCRIPT_DIR, "kb_all.csv")
CATEGORIES_CSV = os.path.join(SCRIPT_DIR, "kb_data_categories.csv")
MDX_DIR = os.path.join(ROOT_DIR, "knowledge_base")  # Output to /knowledge_base in root

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

def sanitize_filename(article_number):
    """Create a safe filename using only the article number"""
    return f"{article_number}.html"

def create_slug(title, id_value):
    """Create a URL-friendly slug from title with ID as fallback"""
    if pd.isna(title) or not str(title).strip():
        return f"article-{id_value}"
    
    # Generate slug from title
    slug = slugify(str(title))
    
    # If title is too short or slug is empty, use ID
    if len(slug) < 3:
        return f"article-{id_value}"
        
    return slug

def clean_control_chars(text):
    """Remove control characters from text"""
    # Remove all control characters except newlines and tabs
    return ''.join(char for char in text if char == '\n' or char == '\t' or not (0 <= ord(char) < 32))

def detect_code_block_language(line):
    """Detect code block language based on content"""
    line_lower = line.lower()
    if any(x in line_lower for x in ['<xml', '<?xml', '<configuration']):
        return 'xml'
    elif any(x in line_lower for x in ['select ', 'from ', 'where ', 'join ', 'group by']):
        return 'sql'
    elif any(x in line_lower for x in ['function', 'class ', 'def ', 'import ', 'export ']):
        return 'javascript' if 'function(' in line_lower else 'python'
    elif any(x in line_lower for x in ['{', '}', ';']) and '=' in line_lower:
        return 'javascript'
    return ''

def format_code_blocks(content):
    """Format code blocks with proper language specification"""
    lines = content.split('\n')
    in_code_block = False
    current_lang = ''
    result = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for code block start
        if line.strip() == '```' or line.strip().startswith('```') and not in_code_block:
            in_code_block = True
            current_lang = line[3:].strip()
            
            # If no language specified, try to detect it
            if not current_lang and i + 1 < len(lines):
                current_lang = detect_code_block_language(lines[i+1])
                
            result.append(f'```{current_lang}' if current_lang else '```')
            i += 1
            continue
            
        # Check for code block end
        if line.strip() == '```' and in_code_block:
            in_code_block = False
            current_lang = ''
            result.append('```')
            i += 1
            continue
            
        result.append(line)
        i += 1
    
    return '\n'.join(result)

def clean_markdown(md_content):
    """Clean up markdown content"""
    if not md_content:
        return ""
    
    import html
    import textwrap
    
    # Convert HTML entities to their corresponding characters
    md_content = html.unescape(md_content)
    
    # Remove control characters (except newlines and tabs)
    md_content = clean_control_chars(md_content)
    
    # Remove empty headers (headers with only whitespace/control chars)
    md_content = re.sub(r'^#+\s*[\x00-\x1F\s]*$', '', md_content, flags=re.MULTILINE)
    
    # Clean up multiple consecutive empty lines
    md_content = re.sub(r'\n{3,}', '\n\n', md_content)
    
    # Remove placeholder sequences (e.g., ****)
    md_content = re.sub(r'\*{4,}', '', md_content)
    
    # Format code blocks with proper language specification
    md_content = format_code_blocks(md_content)
    
    # Process paragraphs and lists for proper spacing
    lines = []
    in_code_block = False
    in_list = False
    
    for line in md_content.split('\n'):
        line = line.strip()
        
        # Handle code blocks
        if line.startswith('```'):
            in_code_block = not in_code_block
            if in_list:
                lines.append('')  # Add extra newline before code block in lists
                in_list = False
            lines.append(line)
            continue
            
        if in_code_block:
            lines.append(line)
            continue
            
        # Skip empty lines (we'll add them back with proper spacing)
        if not line:
            continue
            
        # Handle list items
        if line.startswith(('- ', '* ', '1. ', '2. ')):
            if not in_list and lines and lines[-1]:  # Add newline before first list item
                lines.append('')
            in_list = True
            lines.append(line)
        else:
            if in_list:  # Add newline after list
                lines.append('')
                in_list = False
            lines.append(line)
            lines.append('')  # Add newline after paragraph
    
    # Join lines with appropriate spacing
    md_content = '\n'.join(lines)
    
    # Clean up any triple newlines (shouldn't happen, but just in case)
    md_content = re.sub(r'\n{3,}', '\n\n', md_content)
    
    # Soft wrap long lines in paragraphs (not in lists or code blocks)
    wrapped_lines = []
    in_code_block = False
    in_list = False
    
    for line in md_content.split('\n'):
        if line.startswith('```'):
            in_code_block = not in_code_block
            wrapped_lines.append(line)
        elif line.startswith(('- ', '* ', '1. ', '2. ')):
            in_list = True
            wrapped_lines.append(line)
        elif not line:
            in_list = False
            wrapped_lines.append(line)
        elif in_code_block or in_list or len(line) <= 100:
            wrapped_lines.append(line)
        else:
            wrapped_lines.append('\n'.join(textwrap.wrap(line, width=100)))
    
    # Trim whitespace from start/end
    md_content = md_content.strip()
    
    return md_content

def clean_html(html_content):
    """Convert HTML content to markdown with proper formatting"""
    if not html_content or pd.isna(html_content):
        return ""
        
    # Convert to string in case it's not
    html_content = str(html_content)
    
    try:
        # First convert all HTML to markdown
        md_content = html2markdown.convert(html_content)
        md_content = html.unescape(md_content)
        
        # Clean up any remaining HTML tags that weren't converted
        # But first, we need to protect code blocks
        code_blocks = {}
        
        # Store all code blocks with placeholders
        def store_code_block(match):
            block_id = f"__CODE_BLOCK_{len(code_blocks)}__"
            code_blocks[block_id] = match.group(0)
            return block_id
            
        # Protect fenced code blocks
        md_content = re.sub(r'```[^\n]*\n.*?```', store_code_block, md_content, flags=re.DOTALL)
        
        # Protect inline code
        md_content = re.sub(r'`[^`]+`', store_code_block, md_content)
        
        # Now remove any remaining HTML tags
        md_content = re.sub(r'<[^>]+>', '', md_content)
        
        # Restore code blocks
        for block_id, code in code_blocks.items():
            md_content = md_content.replace(block_id, code)
        
        # Clean up markdown formatting
        md_content = clean_markdown(md_content)
        
        # Fix any double newlines from HTML conversion
        md_content = re.sub(r'\n{3,}', '\n\n', md_content)
        
        # Ensure proper spacing around lists
        # Before lists
        md_content = re.sub(r'([^\n])\n(\s*[-*]\s)', '\1\n\n\2', md_content)
        # After lists
        md_content = re.sub(r'(\n\s*[-*]\s[^\n]*)\n([^\s\n-*])', '\1\n\n\2', md_content)
        
        # Fix any code blocks that might have been broken by the markdown converter
        md_content = re.sub(r'```\s*\n\s*```', '```', md_content)  # Remove empty code blocks
        
        # Fix numbered lists that might have been converted to 1. for each item
        lines = md_content.split('\n')
        in_ol = False
        for i, line in enumerate(lines):
            if re.match(r'^\s*\d+\.\s+', line):
                if not in_ol:
                    in_ol = True
                    lines[i] = re.sub(r'^(\s*)\d+\.\s+', '\1* ', line, count=1)
                else:
                    lines[i] = re.sub(r'^\s*\d+\.\s+', '  * ', line, count=1)
            else:
                in_ol = False
        md_content = '\n'.join(lines)
        
        return md_content.strip()
        
    except Exception as e:
        print(f"Error converting HTML to markdown: {e}")
        # Fallback to basic HTML stripping if conversion fails
        return re.sub(r'<[^>]+>', '', html.unescape(html_content))

def detect_code_language(content):
    """Detect the programming language based on content"""
    content = content.lower()
    if 'powershell' in content or 'get-' in content or '$' in content:
        return 'powershell'
    elif 'sql' in content or 'select ' in content or 'from ' in content:
        return 'sql'
    elif 'http' in content or 'curl' in content:
        return 'bash'
    return ''

def format_code_blocks(content):
    """Format code blocks with proper language detection"""
    # Find all code blocks
    code_blocks = re.findall(r'```(.*?)```', content, re.DOTALL)
    
    for block in code_blocks:
        # Skip if already has language specifier
        if '\n' in block and not block.split('\n', 1)[0].strip():
            code = block.strip()
            lang = detect_code_language(code)
            if lang:
                formatted_block = f'```{lang}\n{code}\n```'
                content = content.replace(f'```{block}```', formatted_block, 1)
    
    return content

def format_frontmatter_value(value):
    """Format frontmatter values for consistent output"""
    if isinstance(value, (list, tuple)):
        if not value:
            return ''
        # Format list as comma-separated string if it's not empty
        return ', '.join(str(v) for v in value if v)
    elif pd.isna(value) or value == '':
        return ''
    return value

def create_mdx_file(article, output_dir, categories):
    """
    Create an MDX file for a single article with categories in the knowledge_base directory
    """
    try:
        # Get article details
        article_id = str(article.get('Id', '')).strip()
        article_number = str(article.get('ArticleNumber', '')).strip()
        title = article.get('Title', 'Untitled').strip()
        
        # Get content and clean it
        content = article.get('Content__c', '')
        if pd.isna(content):
            content = ''
            
        # Clean HTML content
        cleaned_content = clean_html(content)
        
        # Get categories
        article_categories = categories.get(article_id, {})
        product_tags = article_categories.get('product', [])
        
        # Determine the product folder
        folder_name = get_product_folder(product_tags)
        
        # Create the product directory if it doesn't exist
        product_dir = os.path.join(output_dir, folder_name)
        os.makedirs(product_dir, exist_ok=True)
        
        # Use ArticleNumber for the filename
        safe_filename = f"{article_number}.mdx"
        output_path = os.path.join(product_dir, safe_filename)
        
        # Prepare frontmatter
        frontmatter_data = {
            'title': title,  # Keep original title in frontmatter
            'article_number': article_number,
            'id': article_id,
            'products': product_tags or ['Other'],
            'tags': article_categories.get('tag', []),
            'categories': article_categories.get('category', []),
            'last_updated': datetime.now().strftime('%Y-%m-%d')
        }
        
        # Add any additional fields from the article
        for key, value in article.items():
            if pd.notna(value) and key not in ['Id', 'ArticleNumber', 'Title', 'Content__c']:
                frontmatter_data[key.lower()] = format_frontmatter_value(value)
        
        # Format the frontmatter
        fm = '\n'.join([f"{k}: {v}" for k, v in frontmatter_data.items()])
        
        # Create the MDX content
        mdx_content = f"""---
{fm}
---

{cleaned_content}"""
        
        # Write the file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(mdx_content)
            
        return output_path
        
    except Exception as e:
        print(f"Error creating MDX file for article {article_number}: {e}")
        import traceback
        traceback.print_exc()
        return None

def get_product_folder(product_tags):
    """Determine the output folder based on product tags"""
    if not product_tags:
        return 'Other'
    
    # Map old product names to new folder names
    mapped_products = [PRODUCT_MAPPING.get(tag, tag) for tag in product_tags]
    
    # Handle special cases for Activity Monitor and Access Info Center
    special_tags = ['activity_monitor', 'access_info_center']
    
    # Check if any special tags are present
    present_special_tags = [tag for tag in special_tags if tag in [t.lower() for t in product_tags]]
    
    if present_special_tags:
        if len(product_tags) > 1:
            # If article has special tags and other products, use the other product
            other_products = [p for p in mapped_products 
                           if not any(special in p.lower() for special in special_tags)]
            if other_products:
                return other_products[0]
            else:
                return 'Access Analyzer'
        else:
            # If only special tags, use Access Analyzer
            return 'Access Analyzer'
    else:
        # Otherwise, use the first product
        return mapped_products[0] if mapped_products else 'Other'

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
            else:
                categories[parent_id]['product'].append(data_category)
                
    except Exception as e:
        print(f"Error loading categories: {str(e)}")
    
    return categories

def process_csv(test_mode=True, max_articles_per_product=5):
    """
    Process the CSV file and generate MDX files in the knowledge_base directory
    
    Args:
        test_mode (bool): If True, only process a few articles for testing
        max_articles_per_product (int): Maximum number of articles to process per product
    """
    # Create output directory if it doesn't exist
    os.makedirs(MDX_DIR, exist_ok=True)
    
    # Create 'Other' directory for articles without product categories
    os.makedirs(os.path.join(MDX_DIR, 'Other'), exist_ok=True)
    
    # Load categories
    print("Loading categories...")
    categories = load_categories(CATEGORIES_CSV)
    
    # Load the CSV file
    print(f"Loading CSV file: {INPUT_CSV}")
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
        
        encoding = detect_encoding(INPUT_CSV)
        df = pd.read_csv(INPUT_CSV, encoding=encoding, low_memory=False)
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return
    
    print(f"Found {len(df)} articles in the CSV file")
    
    # Track processed articles per product for limiting
    product_counts = defaultdict(int)
    
    # Process each article
    for idx, article in df.iterrows():
        try:
            article_id = str(article.get('Id', '')).strip()
            article_number = str(article.get('ArticleNumber', '')).strip()
            
            if not article_id or not article_number:
                print(f"Skipping article with missing ID or number at index {idx}")
                continue
            
            # Get product categories for this article
            article_categories = categories.get(article_id, {})
            product_tags = article_categories.get('product', [])
            
            # Determine the product folder
            folder_name = get_product_folder(product_tags)
            
            # Check if we've reached the limit for this product
            if test_mode and folder_name in product_counts and product_counts[folder_name] >= max_articles_per_product:
                continue
            
            print(f"Processing article {article_number} - {article.get('Title', 'No Title')}")
            
            # Create MDX file
            mdx_path = create_mdx_file(article, MDX_DIR, categories)
            print(f"  Created: {mdx_path}")
            
            # Update product count
            product_counts[folder_name] += 1
            
            # If in test mode and we've processed enough articles, break
            if test_mode and sum(product_counts.values()) >= (max_articles_per_product * len(PRODUCT_MAPPING)):
                print("Reached maximum number of test articles. Use test_mode=False to process all articles.")
                break
                
        except Exception as e:
            print(f"Error processing article at index {idx}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\nProcessing complete!")
    print(f"Total articles processed: {sum(product_counts.values())}")
    print(f"MDX files saved to: {os.path.abspath(MDX_DIR)}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert KB CSV files to MDX format')
    parser.add_argument('--test', action='store_true', default=True,
                      help='Run in test mode (process only a few articles) (default: True)')
    parser.add_argument('--no-test', dest='test', action='store_false',
                      help='Process all articles')
    parser.add_argument('--max-per-product', type=int, default=5, 
                      help='Maximum number of articles to process per product in test mode (default: 5)')
    
    args = parser.parse_args()
    
    print("=== KB CSV to MDX Converter ===")
    print(f"Input CSV: {os.path.abspath(INPUT_CSV)}")
    print(f"Categories CSV: {os.path.abspath(CATEGORIES_CSV)}")
    print(f"Output directory: {os.path.abspath(MDX_DIR)}")
    print(f"Test mode: {args.test}")
    print(f"Max articles per product: {args.max_per_product}")
    print("=" * 40)
    
    process_csv(test_mode=args.test, max_articles_per_product=args.max_per_product)

if __name__ == "__main__":
    main()
