import os
import pandas as pd
from pathlib import Path
import html
import re
from collections import defaultdict

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

def create_html_file(article, output_dir, categories):
    """Create an HTML file for a single article with categories"""
    # Extract the article number for the filename
    article_id = article.get('Id', '').strip()
    article_number = str(article.get('ArticleNumber', 'unknown')).strip()
    
    # Get categories for this article
    article_categories = categories.get(article_id, {})
    
    # Prepare meta tags for categories
    meta_tags = []
    
    # Add visibility tags
    for tag in article_categories.get('visibility', []):
        meta_tags.append(f'<meta name="visibility" content="{html.escape(tag)}">')
    
    # Add content type tags
    for tag in article_categories.get('content_type', []):
        meta_tags.append(f'<meta name="content_type" content="{html.escape(tag)}">')
    
    # Add former brand tags
    for tag in article_categories.get('former_brand', []):
        meta_tags.append(f'<meta name="former_brand" content="{html.escape(tag)}">')
    
    # Add product tags and prepare for directory structure
    product_tags = article_categories.get('product', [])
    for tag in product_tags:
        meta_tags.append(f'<meta name="product" content="{html.escape(tag)}">')
    
    # Prepare the title and content
    title = html.escape(article.get('Title', 'Untitled Article'))
    content = article.get('Content__c', '')
    
    # Add other fields as meta tags (excluding Change_Log__c)
    for key, value in article.items():
        if key in ['Id', 'Title', 'Content__c', 'ArticleNumber', 'Change_Log__c']:
            continue
            
        if pd.isna(value) or value == '':
            continue
            
        value_str = str(value)
        if len(value_str) > 200:
            value_str = value_str[:200] + '...'
        
        safe_key = html.escape(str(key))
        safe_value = html.escape(value_str)
        meta_tags.append(f'<meta name="{safe_key}" content="{safe_value}">')
    
    # Determine the appropriate folder based on product tags
    if product_tags:
        # Map old product names to new folder names
        mapped_products = [PRODUCT_MAPPING.get(tag, tag) for tag in product_tags]
        
        # Handle special cases for Activity Monitor and Access Info Center
        special_tags = ['activity_monitor', 'access_info_center']
        
        # Check if any special tags are present
        present_special_tags = [tag for tag in special_tags if tag in product_tags]
        
        if present_special_tags:
            if len(product_tags) > 1:
                # If article has special tags and other products, use the other product
                other_products = [p for p in mapped_products 
                                if not any(special in p.lower() for special in special_tags)]
                if other_products:
                    folder_name = other_products[0]
                else:
                    folder_name = 'Access Analyzer'
            else:
                # If only special tags, use Access Analyzer
                folder_name = 'Access Analyzer'
        else:
            # Otherwise, use the first product
            folder_name = mapped_products[0] if mapped_products else 'Other'
    else:
        # No product tags, use 'Other' folder
        folder_name = 'Other'
    
    # Sanitize folder name and create directory
    folder_name = re.sub(r'[\\/*?:"<>|]', '', folder_name)
    output_dir = os.path.join(output_dir, folder_name)
    os.makedirs(output_dir, exist_ok=True)
    
    # Create the filename using only the article number
    filename = sanitize_filename(article_number)
    filepath = os.path.join(output_dir, filename)
    
    # Create the HTML content
    html_parts = [
        '<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f'    <title>{title}</title>',
        '    ' + '\n    '.join(meta_tags),
        '</head>',
        '<body>',
        f'    <h1>{title}</h1>',
        f'    {content}',
        '</body>',
        '</html>'
    ]
    html_content = '\n'.join(html_parts)
    
    # Write to file
    with open(filepath, 'w', encoding='utf-8', errors='replace') as f:
        f.write(html_content)
    
    return filepath

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

def read_csv_with_encoding(file_path, encoding='utf-8'):
    try:
        # First try with UTF-8
        return pd.read_csv(file_path, encoding='utf-8', engine='python')
    except UnicodeDecodeError:
        try:
            # Fall back to latin1 if UTF-8 fails
            return pd.read_csv(file_path, encoding='latin1', engine='python')
        except Exception as e:
            print(f"Error reading {file_path} with latin1 encoding: {e}")
            return None

def main():
    # Set default encoding to UTF-8 for stdout/stderr
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

    # Define paths - output to root kb-html directory
    base_dir = Path(__file__).parent
    root_dir = base_dir.parent  # Go up one level to the root
    csv_path = base_dir / 'kb_all.csv'
    categories_path = base_dir / 'kb_data_categories.csv'
    output_dir = root_dir / 'kb-html'  # Output to root/kb-html
    
    # Load categories
    print("Loading categories...")
    categories = load_categories(categories_path)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the CSV file
    print(f"Starting to process CSV file: {csv_path}")
    df = read_csv_with_encoding(csv_path)
    
    # Ensure required columns exist
    if 'Title' not in df.columns or 'Content__c' not in df.columns:
        print("Error: CSV must contain 'Title' and 'Content__c' columns")
        return
    
    # Convert all columns to string to handle NaN and other non-string values
    df = df.astype(str)
    
    # Exclude archived articles
    if 'PublishStatus' in df.columns:
        archived_count = (df['PublishStatus'] == 'Archived').sum()
        df = df[df['PublishStatus'] != 'Archived']
        print(f"Excluded {archived_count} archived articles")
    
    # Process remaining articles
    max_articles = len(df)
    print(f'Processing {max_articles} active articles')
    
    for idx, row in df.iterrows():
        try:
            filepath = create_html_file(row, output_dir, categories)
            if (idx + 1) % 10 == 0 or idx == 0 or idx == len(df) - 1:
                print(f"Processed {idx + 1}/{len(df)}: {filepath}")
        except Exception as e:
            print(f"Error processing article {idx + 1} (ID: {row.get('Id', 'unknown')}): {str(e)}")
            import traceback
            traceback.print_exc()
    
    print(f"\nProcessing complete!")
    print(f"Successfully processed: {len(df)} articles")
    print(f"HTML files saved to: {output_dir}")

if __name__ == "__main__":
    main()
