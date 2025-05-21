import pandas as pd
import os
import html2markdown
import frontmatter
from slugify import slugify

# Define directories
OUTPUT_DIR = "./kb"
CSV_FILE = "bulkQuery_result_750Qk00000QjyKcIAJ_751Qk00000S8XjfIAF_752Qk00000Owraq.csv"

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Function to convert HTML to markdown
def convert_html_to_markdown(html_content):
    if not html_content or pd.isna(html_content):
        return ""
    return html2markdown.convert(html_content)

# Process the CSV in chunks to handle large files
chunksize = 100
chunk_count = 0

print(f"Starting to process CSV file: {CSV_FILE}")
for chunk in pd.read_csv(CSV_FILE, chunksize=chunksize):
    chunk_count += 1
    print(f"Processing chunk {chunk_count} with {len(chunk)} rows")
    
    for _, row in chunk.iterrows():
        # Get title and content
        title = row.get("Title", "Untitled")
        if pd.isna(title):
            title = "Untitled"
            
        html_content = row.get("Content__c", "")
        
        # Convert HTML to Markdown
        markdown_content = convert_html_to_markdown(html_content)
        
        # Create frontmatter metadata
        metadata = {}
        for key, value in row.items():
            if key != "Content__c" and not pd.isna(value):  # Skip content and NaN values
                metadata[key] = value
                
        # Create slug for filename from title
        file_name = f"{slugify(ArticleNumber)}.mdx"
        file_path = os.path.join(OUTPUT_DIR, file_name)
        
        # Build MDX document
        mdx_doc = frontmatter.Post(markdown_content, **metadata)
        
        # Add title as H1 at the beginning of the content
        markdown_with_title = f"# {title}\n\n{markdown_content}"
        mdx_doc.content = markdown_with_title
        
        # Write to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(frontmatter.dumps(mdx_doc))
            
        print(f"Created: {file_name}")
        
print("CSV file successfully processed") 