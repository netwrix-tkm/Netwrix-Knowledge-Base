import os
import csv
import html
import pandas as pd

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
INPUT_CSV = os.path.join(SCRIPT_DIR, "kb_all.csv")
CATEGORIES_CSV = os.path.join(SCRIPT_DIR, "kb_data_categories.csv")
OUTPUT_DIR = os.path.join(ROOT_DIR, "all-articles-html")

# Product mapping
PRODUCT_MAPPING = {
    'access_info_center': 'access-information-center', 
    'activity_monitor': 'activity-monitor',
    'onesecure': '1secure',
    'auditor': 'auditor',
    'change_tracker': 'change-tracker',
    'data_classification': 'data-classification',
    'endpoint_protector': 'endpoint-protector',
    'groupid': 'directory-manager',
    'log_tracker': 'log-tracker',
    'password_policy_enforcer': 'password-policy-enforcer',
    'password_reset_manager': 'password-reset',
    'password_secure': 'password-secure',
    'policypak': 'endpoint-policy-manager',
    'privilege_secure_endpoints': 'endpoint-privilege-manager',
    'privilege_secure': 'privilege-secure-access-management',
    'privilege_secure_discovery': 'privilege-secure-discovery',
    'recovery_ad': 'recovery-for-active-directory',
    'enterprise_auditor': 'access-analyzer',
    'threat_manager': 'threat-manager',
    'threat_prevention': 'threat-prevention',
    'strongpoint_netsuite': 'platform-governance-netsuite',
    'strongpoint_salesforce': 'platform-governance-salesforce',
    'usercube': 'identity-manager',
    'vulnerability_tracker': 'vulnerability-tracker'
}

def create_html_article(row, output_dir, categories):
    """Create an HTML file for a single article"""
    # Skip archived articles
    if row.get('PublishStatus', '').lower() == 'archived':
        return None

    article_id = row.get('Id', 'unknown')
    content = row.get('Content__c', '')
    title = row.get('Title', 'Untitled')
    
    # Get product folder
    product_folder = get_product_folder(categories, article_id)
    output_folder = os.path.join(output_dir, product_folder)
    os.makedirs(output_folder, exist_ok=True)
    
    # Generate metadata HTML for head
    metadata_html = generate_metadata_html(row)
    
    # Clean up website URL if it exists
    website_url = row.get('Website_Url__c', '')
    if website_url.startswith('<a href="') and '" target=' in website_url:
        website_url = website_url.split('<a href="')[1].split('" target=')[0]
    
    # Create HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)}</title>
    <meta name="article-id" content="{html.escape(article_id)}">
    {metadata_html}"""
    
    # Add website URL if it exists
    if website_url:
        html_content += f'\n    <meta name="website-url" content="{html.escape(website_url)}">'
    
    html_content += f"""
</head>
<body>
    <h1>{html.escape(title)}</h1>
    {content}
</body>
</html>"""

    # Write to file
    output_file = os.path.join(output_folder, f"{article_id}.html")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return output_file

def generate_metadata_html(row):
    """Generate HTML metadata tags for the head section"""
    exclude_fields = {
        'Content__c', 'Change_Log__c', 'Title', 
        'knowledge-article-id', 'recordtypeid', 'PublishStatus',
        'Website_Url__c'
    }
    metadata_html = []
    
    for key, value in sorted(row.items()):
        if key in exclude_fields or pd.isna(value) or value == '':
            continue
            
        # Format the key for the meta tag
        meta_name = key.lower().replace('__c', '').replace('_', '-')
        metadata_html.append(
            f'<meta name="{html.escape(meta_name)}" content="{html.escape(str(value))}">'
        )
    
    return '\n    '.join(metadata_html)

def load_categories():
    """Load the data categories mapping from CSV"""
    categories = {}
    try:
        df = pd.read_csv(CATEGORIES_CSV)
        for _, row in df.iterrows():
            parent_id = row['ParentId']
            category = row['DataCategoryName']
            if parent_id not in categories:
                categories[parent_id] = []
            categories[parent_id].append(category)
        return categories
    except Exception as e:
        print(f"Error loading categories: {e}")
        print(f"Available columns: {df.columns.tolist() if 'df' in locals() else 'No data'}")
        return {}

def get_product_folder(categories, article_id):
    """Determine the product folder based on categories"""
    if article_id not in categories:
        return "uncategorized"
    
    article_categories = categories[article_id]
    
    # Check for exact matches first
    for category in article_categories:
        if category in PRODUCT_MAPPING:
            return PRODUCT_MAPPING[category]
    
    # Fallback to first category with a mapping
    for category in article_categories:
        if category in PRODUCT_MAPPING.values():
            return category
    
    return "uncategorized"

def process_articles(test_mode=False, max_articles_per_product=None):
    """Process the CSV and generate HTML articles"""
    # Load categories
    categories = load_categories()
    
    # Track articles per product
    product_counts = {}
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Process CSV
    processed_count = 0
    with open(INPUT_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            article_id = row.get('Id')
            if not article_id:
                continue
                
            # Skip archived articles
            if row.get('PublishStatus', '').lower() == 'archived':
                continue
                
            # Get product folder
            product_folder = get_product_folder(categories, article_id)
            
            # Check if we've hit the limit for this product
            if max_articles_per_product is not None:
                if product_folder not in product_counts:
                    product_counts[product_folder] = 0
                if product_counts[product_folder] >= max_articles_per_product:
                    continue
                product_counts[product_folder] += 1
            
            # Create HTML article
            output_file = create_html_article(row, OUTPUT_DIR, categories)
            if output_file:  # Only increment if article was created
                print(f"Created: {output_file}")
                processed_count += 1
            
            # Stop after first article in test mode
            if test_mode:
                break
    
    print(f"\nProcessed {processed_count} articles")
    print(f"Output directory: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert KB articles from CSV to HTML')
    parser.add_argument('--test', action='store_true', help='Process only one article for testing')
    parser.add_argument('--max-per-product', type=int, 
                       help='Maximum number of articles to process per product')
    
    args = parser.parse_args()
    
    process_articles(
        test_mode=args.test,
        max_articles_per_product=args.max_per_product
    )