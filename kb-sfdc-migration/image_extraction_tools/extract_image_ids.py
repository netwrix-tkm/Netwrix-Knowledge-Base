import csv
import re
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import time
import json

def extract_image_urls():
    """Extract all image URLs from KB articles"""
    image_urls = set()
    image_params = {}
    image_info = {}  # Store additional info like article titles for context
    
    # Create directory for downloaded images if it doesn't exist
    os.makedirs('kb_images', exist_ok=True)
    
    with open('kb_all.csv', 'r', encoding='utf-8', errors='replace') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        
        # Find the index of important columns
        content_idx = None
        title_idx = None
        for i, column_name in enumerate(header):
            if column_name == 'Content__c':
                content_idx = i
            elif column_name == 'Title':
                title_idx = i
        
        if content_idx is None:
            print("Content__c column not found in CSV file.")
            return None, None, None
            
        print(f"Found Content__c at column index {content_idx}")
        
        # Process each row to find image URLs
        row_count = 0
        for row in csv_reader:
            row_count += 1
            if row_count % 1000 == 0:
                print(f"Processed {row_count} rows...")
                
            if len(row) <= content_idx:
                continue
                
            html_content = row[content_idx]
            if not html_content:
                continue
            
            # Get article title if available
            article_title = row[title_idx] if title_idx is not None and len(row) > title_idx else f"Article #{row_count}"
            
            # Fix double quotes in img tags (common in some exports)
            html_content = html_content.replace('""', '"')
                
            # Parse HTML content
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find all img tags
            img_tags = soup.find_all('img')
            
            # Extract complete image URLs and parameters
            for img_idx, img in enumerate(img_tags):
                src = img.get('src', '')
                if 'rtaImage' in src:
                    # Clean up the URL in case there are encoding issues
                    src = src.replace('&amp;', '&')
                    
                    # Parse URL and get all parameters
                    parsed_url = urlparse(src)
                    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
                    query_params = parse_qs(parsed_url.query)
                    
                    # Store parameters for each URL
                    url_key = (query_params.get('eid', [''])[0], 
                              query_params.get('feoid', [''])[0], 
                              query_params.get('refid', [''])[0])
                    
                    if all(url_key):  # Only store if all parameters are present
                        image_urls.add(src)
                        image_params[src] = {
                            'eid': url_key[0],
                            'feoid': url_key[1],
                            'refid': url_key[2],
                        }
                        
                        # Store additional context
                        filename = f"{url_key[0]}_{url_key[1]}_{url_key[2]}.png"
                        image_info[src] = {
                            'article_title': article_title,
                            'url': src,
                            'params': image_params[src],
                            'filename': filename,
                            'width': img.get('width', ''),
                            'height': img.get('height', ''),
                            'alt': img.get('alt', '')
                        }
    
    print(f"\nFound {len(image_urls)} unique image URLs")
    return image_urls, image_params, image_info

def create_html_viewer(image_urls, image_params, image_info):
    """Create an HTML page to view all images"""
    if not image_urls:
        print("No image URLs available to create viewer.")
        return
        
    # Create HTML page
    with open('image_viewer.html', 'w', encoding='utf-8') as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Salesforce KB Images Viewer</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .image-container { 
            border: 1px solid #ccc; 
            padding: 15px; 
            margin-bottom: 20px; 
            border-radius: 5px; 
        }
        .image-header { 
            display: flex; 
            justify-content: space-between; 
            margin-bottom: 10px; 
            flex-wrap: wrap;
        }
        .image-title { font-weight: bold; flex: 1 1 100%; margin-bottom: 5px; }
        .image-params { color: #666; font-size: 0.9em; width: 100%; margin-bottom: 10px; }
        .image-display { margin: 10px 0; text-align: center; }
        .image-display img { max-width: 100%; border: 1px solid #eee; max-height: 400px; object-fit: contain; }
        .filename { font-family: monospace; color: #0066cc; word-break: break-all; }
        h1 { margin-bottom: 20px; }
        .instructions { background: #f5f5f5; padding: 15px; margin-bottom: 20px; border-radius: 5px; }
        .download-all { margin-bottom: 20px; }
        .download-link {
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            font-size: 14px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
            border: none;
        }
        .download-link:hover {
            background-color: #45a049;
        }
        .controls {
            margin: 10px 0;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        .progress-container {
            width: 100%;
            background-color: #f3f3f3;
            margin: 10px 0;
            border-radius: 4px;
            display: none;
        }
        .progress-bar {
            width: 0%;
            height: 30px;
            background-color: #4CAF50;
            text-align: center;
            line-height: 30px;
            color: white;
            border-radius: 4px;
            transition: width 0.3s;
        }
    </style>
</head>
<body>
    <h1>Salesforce KB Images Viewer</h1>
    
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .image-grid { 
            display: grid; 
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); 
            gap: 15px; 
            margin-top: 20px;
        }
        .image-card { 
            border: 1px solid #ddd; 
            padding: 10px; 
            border-radius: 5px;
            background: #f9f9f9;
        }
        .image-preview {
            max-width: 100%;
            max-height: 150px;
            display: block;
            margin: 0 auto 10px;
            border: 1px solid #eee;
        }
        .filename {
            font-family: monospace;
            font-size: 12px;
            word-break: break-all;
            margin-bottom: 5px;
        }
        .download-btn {
            display: block;
            background: #4CAF50;
            color: white;
            text-align: center;
            padding: 5px;
            text-decoration: none;
            border-radius: 3px;
            margin-top: 5px;
        }
        .download-btn:hover {
            background: #45a049;
        }
    </style>
    
    <h2>Salesforce KB Images</h2>
    <p>Total images: <strong>""" + str(len(image_urls)) + """</strong></p>
    
    <div class="instructions" style="background: #f0f7ff; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h3>How to download:</h3>
        <ol>
            <li>Make sure you're logged into Salesforce in this browser</li>
            <li>Click on any image link below to download it with the correct filename</li>
            <li>For multiple images, right-click and select "Save link as..." on each link</li>
            <li>Or use your browser's "Save Page As" to save all links at once</li>
        </ol>
    </div>
    
    <div class="image-grid">
""")

        # Add each image to the HTML
        for i, url in enumerate(sorted(image_urls)):
            info = image_info.get(url, {})
            filename = info.get('filename', f"image_{i}.png")
            article_title = info.get('article_title', '')
            eid = image_params.get(url, {}).get('eid', '')
            feoid = image_params.get(url, {}).get('feoid', '')
            refid = image_params.get(url, {}).get('refid', '')
            
            f.write(f"""
    <div class="image-card">
        <img src="{url}" 
             class="image-preview"
             alt="{filename}" 
             onerror="this.onerror=null; this.src='data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\' width=\'100\' height=\'100\'><rect width=\'100%\' height=\'100%\' fill=\'#f5f5f5\'/><text x=\'50%\' y=\'50%\' font-family=\'Arial\' font-size=\'10\' text-anchor=\'middle\' dominant-baseline=\'middle\'>Image Preview</text></svg>';"
        >
        <div class="filename">{filename}</div>
        <a href="{url}" class="download-btn" download="{filename}">
            Download
        </a>
    </div>
""")

        f.write("""
    </div>
</body>
</html>
""")

    
    print(f"HTML viewer created: image_viewer.html")
    print(f"Open this file in your web browser while logged into Salesforce to view and download images.")

def main():
    print("Extracting image URLs from KB articles...")
    image_urls, image_params, image_info = extract_image_urls()
    
    if not image_urls:
        print("No image URLs were found.")
        return
    
    # Save URLs to a file
    with open('image_urls.txt', 'w', encoding='utf-8') as f:
        for url in sorted(image_urls):
            params = image_params.get(url, {})
            f.write(f"{url},{params.get('eid', '')},{params.get('feoid', '')},{params.get('refid', '')}\n")
    
    print(f"Image URLs have been written to image_urls.txt")
    
    # Create HTML viewer for manual download
    print("\nCreating HTML viewer for manual image download...")
    create_html_viewer(image_urls, image_params, image_info)
    print("\nNOTE: You'll need to be logged into Salesforce in your browser to view/download the images.")
    print("After downloading the images, you can use create_html_viewer.py to replace URLs in the CSV.")

if __name__ == "__main__":
    main() 