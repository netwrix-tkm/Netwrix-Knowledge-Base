import os
import json
import csv
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

def load_image_info():
    """Load image information from the CSV file"""
    image_info = {}
    if not os.path.exists('image_urls.txt'):
        print("Error: image_urls.txt not found. Run extract_image_ids.py first.")
        return None
        
    with open('image_urls.txt', 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) >= 4:
                url = parts[0]
                image_info[url] = {
                    'url': url,
                    'eid': parts[1],
                    'feoid': parts[2],
                    'refid': parts[3],
                    'filename': f"{parts[1]}_{parts[2]}_{parts[3]}.png"
                }
    
    return image_info

def create_html_viewer():
    """Create an HTML page to view all images"""
    image_info = load_image_info()
    if not image_info:
        return
        
    # Create directory for the HTML page
    os.makedirs('kb_images', exist_ok=True)
    
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
        }
        .image-title { font-weight: bold; }
        .image-params { color: #666; font-size: 0.9em; }
        .image-display { margin: 10px 0; text-align: center; }
        .image-display img { max-width: 100%; border: 1px solid #eee; }
        .github-url { font-family: monospace; margin-top: 10px; }
        .filename { font-family: monospace; color: #0066cc; }
        h1 { margin-bottom: 20px; }
        .instructions { background: #f5f5f5; padding: 15px; margin-bottom: 20px; border-radius: 5px; }
        .download-all { margin-bottom: 20px; }
        .download-button {
            background-color: #4CAF50;
            color: white;
            padding: 5px 10px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 10px;
        }
        /* Progress indicator */
        #progress-bar {
            width: 100%;
            background-color: #f1f1f1;
            padding: 3px;
            border-radius: 3px;
            box-sizing: border-box;
            margin-bottom: 20px;
            display: none;
        }
        #progress-bar-inner {
            height: 24px;
            background-color: #4CAF50;
            text-align: center;
            line-height: 24px;
            color: white;
            border-radius: 2px;
            transition: width 0.3s;
        }
        .download-all-button {
            background-color: #0066cc;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h1>Salesforce KB Images Viewer</h1>
    
    <div class="instructions">
        <h3>Instructions:</h3>
        <ol>
            <li>Ensure you're logged into your Salesforce account in this browser</li>
            <li>The images below should load if your authentication is active</li>
            <li>Use the "Download Image" buttons to save each image with the correct filename</li>
            <li>After downloading all images, you can upload them to GitHub and use the replacement script</li>
        </ol>
    </div>
    
    <div class="download-all">
        <p>Total images: <strong>""" + str(len(image_info)) + """</strong></p>
        <button id="download-all-button" class="download-all-button" onclick="downloadAllImages()">Download All Images</button>
        <div id="progress-bar">
            <div id="progress-bar-inner">0%</div>
        </div>
        <div id="download-status"></div>
    </div>

    <script>
        // Array to store all image info
        const imageInfo = [
""")

        # Add image info as JavaScript array
        for i, (url, info) in enumerate(sorted(image_info.items(), key=lambda x: x[1].get('filename', ''))):
            filename = info.get('filename', '')
            f.write(f"""            {{
                url: "{url}",
                filename: "{filename}",
                eid: "{info.get('eid', '')}",
                feoid: "{info.get('feoid', '')}",
                refid: "{info.get('refid', '')}"
            }}""")
            if i < len(image_info) - 1:
                f.write(",\n")
            else:
                f.write("\n")

        f.write("""        ];
        
        // Function to download a single image
        function downloadImage(url, filename) {
            // Create a hidden link element
            const link = document.createElement('a');
            link.href = url;
            link.download = filename;
            link.style.display = 'none';
            document.body.appendChild(link);
            
            // Click the link to trigger download
            link.click();
            
            // Clean up
            setTimeout(() => {
                document.body.removeChild(link);
            }, 100);
        }
        
        // Function to download all images with delay
        async function downloadAllImages() {
            const delayMs = 500; // Delay between downloads in milliseconds
            const progressBar = document.getElementById('progress-bar');
            const progressBarInner = document.getElementById('progress-bar-inner');
            const downloadStatus = document.getElementById('download-status');
            const downloadButton = document.getElementById('download-all-button');
            
            // Show progress bar
            progressBar.style.display = 'block';
            downloadButton.disabled = true;
            downloadButton.textContent = 'Downloading...';
            
            let completed = 0;
            const total = imageInfo.length;
            
            for (let i = 0; i < imageInfo.length; i++) {
                const info = imageInfo[i];
                
                // Update status
                downloadStatus.textContent = `Downloading ${i+1} of ${total}: ${info.filename}`;
                
                try {
                    // Download image
                    downloadImage(info.url, info.filename);
                    
                    // Update progress
                    completed++;
                    const percentage = Math.round((completed / total) * 100);
                    progressBarInner.style.width = percentage + '%';
                    progressBarInner.textContent = percentage + '%';
                    
                    // Wait before next download
                    await new Promise(resolve => setTimeout(resolve, delayMs));
                } catch (error) {
                    console.error(`Error downloading ${info.filename}:`, error);
                }
            }
            
            // Download complete
            downloadStatus.textContent = `Download complete! ${completed} of ${total} images downloaded.`;
            downloadButton.textContent = 'Download Complete';
        }
    </script>
""")

        # Add each image to the HTML
        for i, (url, info) in enumerate(sorted(image_info.items(), key=lambda x: x[1].get('filename', ''))):
            filename = info.get('filename', '')
            f.write(f"""
    <div class="image-container">
        <div class="image-header">
            <span class="image-title">Image {i+1}/{len(image_info)}</span>
            <span class="filename">{filename}</span>
        </div>
        <div class="image-params">
            EID: {info.get('eid', '')}<br>
            FEOID: {info.get('feoid', '')}<br>
            REFID: {info.get('refid', '')}
        </div>
        <div class="image-display">
            <img src="{url}" alt="KB Image" onerror="this.onerror=null; this.src=''; this.alt='Image failed to load - authentication may be required';">
        </div>
        <button class="download-button" onclick="downloadImage('{url}', '{filename}')">Download Image ({filename})</button>
    </div>
""")
        
        f.write("""
</body>
</html>
""")
    
    print(f"HTML viewer created: image_viewer.html")
    print(f"Open this file in your browser while logged into Salesforce to view and download images.")

def replace_image_urls_in_csv():
    """Replace Salesforce image URLs with GitHub URLs in the CSV file"""
    # Check if necessary files exist
    if not os.path.exists('kb_all.csv'):
        print("Error: kb_all.csv not found.")
        return
    
    if not os.path.exists('image_urls.txt'):
        print("Error: image_urls.txt not found. Run extract_image_ids.py first.")
        return
        
    # Load image information
    image_info = load_image_info()
    if not image_info:
        return
        
    # Ask for GitHub repository information
    print("\nEnter GitHub information for URL replacement:")
    github_org = input("GitHub organization name: ")
    github_repo = input("GitHub repository name: ")
    github_branch = input("GitHub branch (default: main): ") or "main"
    github_path = input("Path to images in repository (default: images/): ") or "images/"
    
    # Ensure path ends with '/'
    if not github_path.endswith('/'):
        github_path += '/'
        
    # Create backup of original file
    backup_file = 'kb_all_original.csv'
    if not os.path.exists(backup_file):
        with open('kb_all.csv', 'rb') as src, open(backup_file, 'wb') as dst:
            dst.write(src.read())
        print(f"Backup created: {backup_file}")
        
    # Read the CSV file and replace image URLs
    with open('kb_all.csv', 'r', encoding='utf-8', errors='replace') as infile:
        csv_reader = csv.reader(infile)
        header = next(csv_reader)
        
        # Find the index of the Content__c column
        content_idx = None
        for i, column_name in enumerate(header):
            if column_name == 'Content__c':
                content_idx = i
                break
        
        if content_idx is None:
            print("Content__c column not found in CSV file.")
            return
            
        # Prepare output file
        with open('kb_all_github_urls.csv', 'w', encoding='utf-8', newline='') as outfile:
            csv_writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(header)
            
            # Process each row
            rows_processed = 0
            urls_replaced = 0
            
            for row in csv_reader:
                rows_processed += 1
                if len(row) <= content_idx:
                    csv_writer.writerow(row)
                    continue
                    
                html_content = row[content_idx]
                if not html_content:
                    csv_writer.writerow(row)
                    continue
                
                # Fix double quotes in img tags (common in some exports)
                html_content = html_content.replace('""', '"')
                    
                # Parse HTML content
                soup = BeautifulSoup(html_content, 'html.parser')
                
                # Find all img tags
                img_tags = soup.find_all('img')
                
                # Replace URLs
                replacements_in_row = 0
                for img in img_tags:
                    src = img.get('src', '')
                    if src in image_info:
                        # Replace with GitHub URL
                        filename = image_info[src].get('filename', '')
                        new_url = f"https://raw.githubusercontent.com/{github_org}/{github_repo}/{github_branch}/{github_path}{filename}"
                        img['src'] = new_url
                        replacements_in_row += 1
                        urls_replaced += 1
                
                if replacements_in_row > 0:
                    # Update the row with new content
                    row[content_idx] = str(soup)
                    
                csv_writer.writerow(row)
                
                if rows_processed % 1000 == 0:
                    print(f"Processed {rows_processed} rows...")
    
    print(f"\nReplacement complete:")
    print(f"- Processed {rows_processed} rows")
    print(f"- Replaced {urls_replaced} image URLs")
    print(f"- Output file: kb_all_github_urls.csv")

def main():
    print("\nKB Image Viewer and URL Replacement Tool\n")
    print("1. Create HTML viewer for images")
    print("2. Replace Salesforce image URLs with GitHub URLs in CSV")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == '1':
        create_html_viewer()
    elif choice == '2':
        replace_image_urls_in_csv()
    elif choice == '3':
        print("Exiting.")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 