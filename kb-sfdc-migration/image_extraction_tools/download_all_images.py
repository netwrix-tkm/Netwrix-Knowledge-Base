import os
import json
import time
import argparse
import browser_cookie3
import requests
from tqdm import tqdm

def load_image_urls():
    """Load image URLs from the text file"""
    if not os.path.exists('image_urls.txt'):
        print("Error: image_urls.txt not found. Run extract_image_ids.py first.")
        return None
    
    urls = []
    with open('image_urls.txt', 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) >= 4:
                url = parts[0]
                filename = f"{parts[1]}_{parts[2]}_{parts[3]}.png"
                urls.append((url, filename))
    
    return urls

def create_cookie_guide():
    """Create a guide on how to manually export cookies"""
    with open('cookie_guide.txt', 'w', encoding='utf-8') as f:
        f.write("""HOW TO EXPORT YOUR SALESFORCE COOKIES
=================================

1. Make sure you're logged into Salesforce in your browser
2. Press F12 to open developer tools
3. Go to the "Application" tab (or "Storage" in Firefox)
4. In the left sidebar, expand "Cookies" and select your Salesforce domain
5. Right-click and select "Copy" or "Export" (varies by browser)
6. If "Export" is available, save the file as "salesforce_cookies.json"
7. If "Copy" is the only option, paste into a new file called "salesforce_cookies.json"

The file should look something like this:
[
  {
    "name": "cookie_name",
    "value": "cookie_value",
    "domain": ".force.com",
    "path": "/",
    "expires": 1234567890,
    "httpOnly": true,
    "secure": true
  },
  ...more cookies...
]

Save this file in the same directory as the script.
""")
    
    print("Created cookie guide: cookie_guide.txt")
    print("Please follow the instructions in the guide to export your Salesforce cookies.")
    return

def download_all_images(browser='chrome', delay=0.5, manual_cookies=None):
    """Download all images using browser cookies for authentication"""
    # Load image URLs
    image_urls = load_image_urls()
    if not image_urls:
        print("No image URLs found.")
        return
    
    # Create directory for downloaded images if it doesn't exist
    os.makedirs('kb_images', exist_ok=True)
    
    print(f"\nPreparing to download {len(image_urls)} images...")
    
    # Initialize cookies
    cookies = None
    
    # Try to load manual cookies if specified
    if manual_cookies:
        try:
            if os.path.exists(manual_cookies):
                with open(manual_cookies, 'r') as f:
                    cookie_data = json.load(f)
                print(f"Successfully loaded {len(cookie_data)} cookies from {manual_cookies}")
                # Convert to cookie jar
                cookies = {}
                for cookie in cookie_data:
                    cookies[cookie['name']] = cookie['value']
            else:
                print(f"Cookie file {manual_cookies} not found.")
                create_cookie_guide()
                return
        except Exception as e:
            print(f"Error loading manual cookies: {str(e)}")
            create_cookie_guide()
            return
    else:
        # Try to get cookies from browser
        print(f"Using cookies from: {browser}")
        try:
            if browser.lower() == 'chrome':
                cookies = browser_cookie3.chrome()
            elif browser.lower() == 'firefox':
                cookies = browser_cookie3.firefox()
            elif browser.lower() == 'edge':
                cookies = browser_cookie3.edge()
            elif browser.lower() == 'safari':
                cookies = browser_cookie3.safari()
            elif browser.lower() == 'opera':
                cookies = browser_cookie3.opera()
            else:
                print(f"Unsupported browser: {browser}. Using Chrome.")
                cookies = browser_cookie3.chrome()
            
            print("Successfully loaded browser cookies.")
        except Exception as e:
            print(f"Error loading cookies: {str(e)}")
            print("Creating guide for manual cookie export...")
            create_cookie_guide()
            return
    
    # Create a session with the cookies
    session = requests.Session()
    if cookies:
        if isinstance(cookies, dict):
            # Manual cookies as dictionary
            for name, value in cookies.items():
                session.cookies.set(name, value)
        else:
            # Browser cookies from browser_cookie3
            session.cookies.update(cookies)
    
    # Set headers to mimic browser
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://nwxcorp.lightning.force.com/'
    })
    
        # Test the authentication    print("Testing authentication...")    try:        test_url = "https://nwxcorp.lightning.force.com"        test_resp = session.get(test_url, timeout=10)        if 'login' in test_resp.url.lower():            print("WARNING: Authentication may not be valid. Continuing anyway, but expect failures.")        else:            print("Authentication test successful!")                # Test an actual image URL to make sure we can access it        if image_urls and image_urls[0]:            print("\nTesting image URL access...")            test_img_url, _ = image_urls[0]            img_resp = session.get(test_img_url, stream=True, timeout=10)            content_type = img_resp.headers.get('Content-Type', '')            print(f"Response status: {img_resp.status_code}")            print(f"Content type: {content_type}")                        if 'image' in content_type.lower():                print("Image URL test successful!")            elif content_type.startswith('text/html'):                print("WARNING: Image URL returned HTML, likely a login page.")                print("The downloaded files might not be actual images.")                print("Let's check if the OneDrive path is causing permission issues...")                                # Try to create a test file                try:                    test_file = os.path.join('kb_images', 'test_file.txt')                    with open(test_file, 'w') as f:                        f.write('Test file')                    print(f"Successfully created test file: {test_file}")                                        # File exists, so permissions are good                    try:                        os.remove(test_file)                        print("Test file removed successfully.")                    except:                        pass                except Exception as e:                    print(f"ERROR: Could not create test file in kb_images directory: {str(e)}")                    print("This might be a permissions issue with OneDrive.")                    print("Try running this script from a non-OneDrive location.")            else:                print(f"WARNING: Unexpected content type for image URL: {content_type}")    except Exception as e:        print(f"Authentication test failed: {str(e)}")        print("Continuing anyway...")
    
    # Download each image with progress bar
    stats = {'success': 0, 'failed': 0, 'skipped': 0}
    failed_urls = []
    
    with tqdm(total=len(image_urls), desc="Downloading images") as pbar:
        for url, filename in image_urls:
            filepath = os.path.join('kb_images', filename)
            
            # Skip if file already exists
            if os.path.exists(filepath):
                stats['skipped'] += 1
                pbar.update(1)
                continue
            
            try:
                # Download the image
                response = session.get(url, stream=True, timeout=30)
                
                if response.status_code == 200:
                                    # Check if it's actually an image or HTML login page                    content_type = response.headers.get('Content-Type', '')                    if content_type.startswith('text/html'):                        # This might be a login page, let's check more carefully                        content = response.content.decode('utf-8', errors='ignore')                        if 'login' in content.lower() or 'sign in' in content.lower() or 'authentication' in content.lower():                            print(f"\nWarning: Got HTML login page instead of image for {url}")                            failed_urls.append((url, f"Got HTML login page instead of image (auth required)"))                            stats['failed'] += 1                        else:                            # HTML but not login page, try to save it anyway and mark as potential failure                            print(f"\nWarning: Got HTML instead of image for {url}, saving anyway")                            with open(filepath, 'wb') as f:                                f.write(response.content)                                                        # Also save HTML version for inspection                            html_path = filepath + '.html'                            with open(html_path, 'wb') as f:                                f.write(response.content)                                                            failed_urls.append((url, f"Got HTML instead of image, saved both formats for inspection"))                            stats['failed'] += 1                    else:                        # Save the image                        try:                            with open(filepath, 'wb') as f:                                for chunk in response.iter_content(chunk_size=8192):                                    f.write(chunk)                            print(f"\nSaved image: {filepath}")                            file_size = os.path.getsize(filepath)                            print(f"File size: {file_size} bytes")                            stats['success'] += 1                        except Exception as e:                            print(f"\nError saving image {filepath}: {str(e)}")                            failed_urls.append((url, f"Error saving file: {str(e)}"))                            stats['failed'] += 1
                else:
                    failed_urls.append((url, f"Status code: {response.status_code}"))
                    stats['failed'] += 1
            except Exception as e:
                failed_urls.append((url, str(e)))
                stats['failed'] += 1
            
            pbar.update(1)
            
            # Add delay to avoid overwhelming the server
            if delay > 0:
                time.sleep(delay)
    
    # Save failed URLs to file
    if failed_urls:
        with open('failed_downloads.txt', 'w', encoding='utf-8') as f:
            for url, reason in failed_urls:
                f.write(f"{url},{reason}\n")
    
    print(f"\nDownload summary:")
    print(f"- Success: {stats['success']}")
    print(f"- Failed: {stats['failed']}")
    print(f"- Skipped (already exist): {stats['skipped']}")
    
    if stats['failed'] > 0:
        print(f"\nFailed URLs saved to: failed_downloads.txt")
        print("Most failures are likely due to authentication issues.")
        print("To solve this, open image_viewer.html in your browser where you're logged into Salesforce")
        print("and manually save those images.")
    
    if stats['success'] > 0:
        print(f"\nImages saved to the 'kb_images' directory.")
        print("You can now upload these images to GitHub and update your KB articles.")

def main():
    parser = argparse.ArgumentParser(description='Download all KB images using browser cookies')
    parser.add_argument('--browser', '-b', type=str, default='chrome',
                        choices=['chrome', 'firefox', 'edge', 'safari', 'opera'],
                        help='Browser to get cookies from (default: chrome)')
    parser.add_argument('--delay', '-d', type=float, default=0.5,
                       help='Delay between downloads in seconds (default: 0.5)')
    parser.add_argument('--cookies', '-c', type=str, default=None,
                       help='Path to a JSON file containing manually exported cookies')
    
    args = parser.parse_args()
    
    download_all_images(browser=args.browser, delay=args.delay, manual_cookies=args.cookies)

if __name__ == "__main__":
    main() 