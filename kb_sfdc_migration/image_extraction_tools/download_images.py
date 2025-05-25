import os
import requests
import re
import base64
import json
import time
import uuid
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs, urljoin
from pathlib import Path
from dotenv import load_dotenv
from simple_salesforce import Salesforce

# Load environment variables from .env file in the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(root_dir, '.env'))

def read_image_urls(file_path):
    """Read image URLs and extract feoid from the text file."""
    image_data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
                
            # Split the line into URL and metadata
            parts = line.split(',')
            if len(parts) < 2:
                continue
                
            url = parts[0].strip()
            # The feoid is the third part (index 2) in the metadata
            feoid = parts[2].strip() if len(parts) > 2 else None
            
            if url and feoid and 'rtaImage' in url:
                image_data.append({
                    'url': url,
                    'feoid': feoid
                })
    return image_data

def extract_content_document_id(url):
    """Extract the content document ID from the URL."""
    # Example URL: https://nwxcorp.file.force.com/servlet/rtaImage?eid=ka04u0000001COn&feoid=00N0g000004CA0p&refid=0EM4u000004bUo6
    # The 'eid' parameter is the content document ID
    from urllib.parse import urlparse, parse_qs
    
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    return params.get('eid', [None])[0]

def get_content_download_url(session, instance_url, content_document_id):
    """Get the download URL for a content document using the Salesforce REST API."""
    # First, get the content version ID
    query_url = f"{instance_url}/services/data/v56.0/query"
    query = f"SELECT ContentDocumentId, LatestPublishedVersionId FROM ContentDocument WHERE Id = '{content_document_id}'"
    
    response = session.get(query_url, params={'q': query})
    response.raise_for_status()
    result = response.json()
    
    if not result['records']:
        raise Exception(f"No content document found with ID {content_document_id}")
    
    content_version_id = result['records'][0]['LatestPublishedVersionId']
    
    # Now get the download URL for the content version
    content_version_url = f"{instance_url}/services/data/v56.0/sobjects/ContentVersion/{content_version_id}"
    response = session.get(content_version_url)
    response.raise_for_status()
    
    version_data = response.json()
    download_url = version_data.get('VersionDataUrl')
    
    if not download_url:
        raise Exception(f"No download URL found for content version {content_version_id}")
    
    # Make sure the URL is absolute
    if not download_url.startswith('http'):
        download_url = f"{instance_url}{download_url}"
    
    return download_url

def download_images(image_data, session_cookie, output_dir='kb-images'):
    print(f"Starting download with session cookie: {session_cookie[:10]}...")  # Log first 10 chars of cookie
    """Download images using the provided session cookie."""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize a session to handle cookies
    session = requests.Session()
    
    # Set up headers for Salesforce API
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'DNT': '1'
    }
    
    # Set the session cookie for the Salesforce domain
    instance_url = 'https://nwxcorp.my.salesforce.com'
    session.cookies.set('sid', session_cookie, domain='.salesforce.com')
    session.cookies.set('sid', session_cookie, domain='nwxcorp.my.salesforce.com')
    session.headers.update(headers)
    
    downloaded = {}
    errors = []
    
    for i, img in enumerate(image_data, 1):
        url = img['url']
        feoid = img['feoid']
        
        try:
            # Determine file extension from URL or use default .png
            parsed_url = urlparse(url)
            path = parsed_url.path.lower()
            ext = '.png'  # default extension
            
            # Try to get extension from URL path
            if '.' in path:
                path_ext = path[path.rfind('.'):]
                if len(path_ext) <= 5:  # Reasonable length for file extensions
                    ext = path_ext
            
            filename = f"{feoid}{ext}"
            filepath = os.path.join(output_dir, filename)
            
            # Skip if already downloaded
            if os.path.exists(filepath):
                print(f"[{i}/{len(image_data)}] Skipping {filename} - already exists")
                downloaded[url] = filename
                continue
                
            print(f"\n[{i}/{len(image_data)}] Downloading {url}")
            print(f"  Using cookie: sid={session_cookie[:10]}...")  # Log first 10 chars of cookie
            
            try:
                print(f"\nProcessing image {i}/{len(image_data)}")
                print(f"  Original URL: {url}")
                
                # Extract the content document ID from the URL
                content_document_id = extract_content_document_id(url)
                if not content_document_id:
                    error_msg = f"Could not extract content document ID from URL: {url}"
                    print(f"  {error_msg}")
                    errors.append(error_msg)
                    continue
                    
                print(f"  Content Document ID: {content_document_id}")
                
                # Get the download URL using the Salesforce REST API
                try:
                    print("  Getting download URL from Salesforce API...")
                    download_url = get_content_download_url(session, instance_url, content_document_id)
                    print(f"  Download URL: {download_url}")
                except Exception as e:
                    error_msg = f"Error getting download URL for {content_document_id}: {str(e)}"
                    print(f"  {error_msg}")
                    errors.append(error_msg)
                    continue
                
                # Download the file
                try:
                    print("  Downloading file...")
                    response = session.get(download_url, stream=True, timeout=60)
                    response.raise_for_status()
                    
                    # Check content type
                    content_type = response.headers.get('content-type', '').lower()
                    print(f"  Content-Type: {content_type}")
                    
                    if 'text/html' in content_type:
                        raise Exception("Received HTML instead of image data")
                    
                    # Determine file extension from content type
                    ext = '.bin'  # default extension
                    if 'jpeg' in content_type or 'jpg' in content_type:
                        ext = '.jpg'
                    elif 'png' in content_type:
                        ext = '.png'
                    elif 'gif' in content_type:
                        ext = '.gif'
                    elif 'svg' in content_type:
                        ext = '.svg'
                    
                    # Save the file
                    filename = f"{feoid}{ext}"
                    filepath = os.path.join(output_dir, filename)
                    
                    with open(filepath, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    
                    print(f"  Successfully saved to {filepath}")
                    downloaded[url] = filename
                    
                except requests.exceptions.RequestException as e:
                    error_msg = f"Error downloading file: {str(e)}"
                    print(f"  {error_msg}")
                    errors.append(f"{url}: {error_msg}")
                    continue
                
            except Exception as e:
                error_msg = f"Unexpected error processing {url}: {str(e)}"
                print(f"  {error_msg}")
                errors.append(error_msg)
                continue
            
            # Check content type for extension
            content_type = response.headers.get('content-type', '')
            if 'jpeg' in content_type or 'jpg' in content_type:
                ext = '.jpg'
            elif 'png' in content_type:
                ext = '.png'
            elif 'gif' in content_type:
                ext = '.gif'
            elif 'svg' in content_type:
                ext = '.svg'
                
            # Update filename with correct extension
            filename = f"{feoid}{ext}"
            filepath = os.path.join(output_dir, filename)
            
            # Save the image
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            downloaded[url] = filename
            print(f"Saved as {filename}")
            
        except Exception as e:
            error_msg = f"Error downloading {url}: {str(e)}"
            print(error_msg)
            errors.append(error_msg)
    
    return downloaded, errors

class SalesforceJWT:
    def __init__(self):
        self.client_id = os.getenv('SF_CLIENT_ID')
        self.username = os.getenv('SF_USERNAME')
        self.domain = os.getenv('SF_DOMAIN', 'login')  # or 'test' for sandbox
        self.instance = os.getenv('SF_INSTANCE', 'nwxcorp')
        # Look for salesforce.key in the root directory
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.private_key_path = os.path.normpath(os.path.join(root_dir, 'salesforce.key'))
        print(f"Looking for private key at: {self.private_key_path}")
        # Verify the file exists and is readable
        if not os.path.isfile(self.private_key_path):
            raise FileNotFoundError(f"Private key file not found at: {self.private_key_path}")
        if not os.access(self.private_key_path, os.R_OK):
            raise PermissionError(f"No read permission for private key file: {self.private_key_path}")
        self.consumer_key = os.getenv('CONSUMER_KEY', self.client_id)
        self.audience = os.getenv('AUDIENCE', 'https://login.salesforce.com')
        
        self.access_token = None
        self.instance_url = None
        self.session = requests.Session()
        
        if not all([self.client_id, self.username]):
            raise ValueError("Missing required Salesforce credentials in .env file")
    
    def _read_private_key(self):
        """Read the private key from file"""
        try:
            print(f"Reading private key from: {self.private_key_path}")
            with open(self.private_key_path, 'r') as f:
                key_content = f.read()
            return key_content
        except Exception as e:
            raise Exception(f"Failed to read private key: {str(e)}")
    
    def authenticate(self):
        """Authenticate with Salesforce using JWT Bearer Flow"""
        print("Starting JWT Bearer authentication...")
        
        try:
            import jwt
            import time
            import json
            
            # Read the private key
            private_key = self._read_private_key()
            print("Successfully read private key")
            
            # JWT claims
            issued_at = int(time.time())
            expiration = issued_at + 300  # 5 minutes from now
            
            # Create the JWT token
            jwt_payload = {
                'iss': self.consumer_key,
                'sub': self.username,
                'aud': f'https://{self.domain}.salesforce.com',
                'exp': expiration,
                'iat': issued_at
            }
            
            print("Generating JWT token...")
            print("JWT Payload:", json.dumps(jwt_payload, indent=2))
            print("Private key starts with:", private_key[:50].strip() + "...")
            
            encoded_jwt = jwt.encode(
                jwt_payload,
                private_key,
                algorithm='RS256',
                headers={'alg': 'RS256'}
            )
            print("JWT Token generated successfully")
            
            print("Exchanging JWT for access token...")
            token_url = f'https://{self.domain}.salesforce.com/services/oauth2/token'
            token_data = {
                'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
                'assertion': encoded_jwt
            }
            
            response = requests.post(token_url, data=token_data)
            response.raise_for_status()
            token_info = response.json()
            
            if 'access_token' not in token_info:
                raise Exception("No access token in response")
            
            print("Authentication successful!")
            print(f"Instance URL: {token_info['instance_url']}")
            
            return {
                'access_token': token_info['access_token'],
                'instance_url': token_info['instance_url']
            }
            
        except Exception as e:
            print(f"Authentication error: {str(e)}")
            if hasattr(e, 'response'):
                print(f"Error details: {e.response.text}")
            return False
    
    def get_content_document_data(self, content_document_id):
        """Get content document data using the Salesforce REST API"""
        try:
            # First, get the content version ID
            query_url = f"{self.instance_url}/services/data/v56.0/query"
            query = f"SELECT Id, Title, FileType, ContentSize, LatestPublishedVersionId FROM ContentDocument WHERE Id = '{content_document_id}'"
            
            response = self.session.get(query_url, params={'q': query}, timeout=30)
            response.raise_for_status()
            result = response.json()
            
            if not result['records']:
                raise Exception(f"No content document found with ID {content_document_id}")
            
            return result['records'][0]
            
        except Exception as e:
            print(f"Error getting content document data: {str(e)}")
            return None
    
    def download_file(self, content_version_id, output_path):
        """Download a file using the ContentVersion ID"""
        try:
            # First, get the file metadata
            file_url = f"{self.instance_url}/services/data/v56.0/sobjects/ContentVersion/{content_version_id}"
            response = self.session.get(file_url)
            response.raise_for_status()
            file_data = response.json()
            
            # Get the download URL
            download_url = f"{self.instance_url}/services/data/v56.0/sobjects/ContentVersion/{content_version_id}/VersionData"
            
            # Download the file
            response = self.session.get(download_url, stream=True)
            response.raise_for_status()
            
            # Determine file extension from file type or content type
            file_extension = file_data.get('FileExtension', '').lower()
            if not file_extension:
                content_type = response.headers.get('content-type', '').lower()
                if 'jpeg' in content_type or 'jpg' in content_type:
                    file_extension = 'jpg'
                elif 'png' in content_type:
                    file_extension = 'png'
                elif 'gif' in content_type:
                    file_extension = 'gif'
                else:
                    file_extension = 'bin'
            
            # Ensure the output path has the correct extension
            if not output_path.lower().endswith(f'.{file_extension}'):
                output_path = f"{os.path.splitext(output_path)[0]}.{file_extension}"
            
            # Save the file
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            print(f"Successfully downloaded to {output_path}")
            return output_path
            
        except Exception as e:
            print(f"Error downloading file: {str(e)}")
            return None

def extract_content_document_id(url):
    """Extract the content document ID from the URL."""
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    return params.get('eid', [None])[0]

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize Salesforce JWT authentication
    try:
        print("Initializing Salesforce JWT authentication...")
        sf = SalesforceJWT()
        if not sf.authenticate():
            print("Failed to authenticate with Salesforce. Please check your credentials and private key.")
            return
            
        print(f"Connected to Salesforce instance: {sf.instance_url}")
        
    except Exception as e:
        print(f"Error initializing Salesforce connection: {str(e)}")
        return
    
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the image URLs file (in the same directory as this script)
    urls_file = os.path.join(script_dir, 'image_urls.txt')
    
    # Output directory (relative to the script)
    output_dir = os.path.join(script_dir, 'kb-images')
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the image URLs
    print(f"\nReading image URLs from {urls_file}...")
    all_image_data = read_image_urls(urls_file)
    
    if not all_image_data:
        print("No image URLs found in the file.")
        return
    
    print(f"Found {len(all_image_data)} image URLs.")
    
    # Only process the first 10 images for testing
    image_data = all_image_data[:10]
    print(f"\nProcessing first {len(image_data)} images for testing...")
    
    downloaded = []
    errors = []
    
    for i, img in enumerate(image_data, 1):
        url = img['url']
        feoid = img['feoid']
        
        print(f"\n[{i}/{len(image_data)}] Processing {url}")
        
        try:
            # Extract content document ID from URL
            content_document_id = extract_content_document_id(url)
            if not content_document_id:
                error_msg = f"Could not extract content document ID from URL: {url}"
                print(f"  {error_msg}")
                errors.append(error_msg)
                continue
            
            print(f"  Content Document ID: {content_document_id}")
            
            # Get content document data
            print("  Fetching document metadata...")
            doc_data = sf.get_content_document_data(content_document_id)
            if not doc_data:
                error_msg = f"Could not retrieve document data for {content_document_id}"
                print(f"  {error_msg}")
                errors.append(error_msg)
                continue
            
            content_version_id = doc_data.get('LatestPublishedVersionId')
            if not content_version_id:
                error_msg = f"No published version found for document {content_document_id}"
                print(f"  {error_msg}")
                errors.append(error_msg)
                continue
            
            # Determine output filename
            file_extension = doc_data.get('FileExtension', 'bin').lower()
            output_path = os.path.join(output_dir, f"{feoid}.{file_extension}")
            
            # Download the file
            print(f"  Downloading version {content_version_id} to {output_path}")
            result = sf.download_file(content_version_id, output_path)
            
            if result:
                print(f"  Successfully downloaded to {result}")
                downloaded.append({
                    'url': url,
                    'feoid': feoid,
                    'local_path': result
                })
            else:
                error_msg = f"Failed to download {content_document_id}"
                print(f"  {error_msg}")
                errors.append(f"{url}: {error_msg}")
                
        except Exception as e:
            error_msg = f"Error processing {url}: {str(e)}"
            print(f"  {error_msg}")
            errors.append(f"{url}: {error_msg}")
            continue
    
    # Print summary
    print("\n=== Download Summary ===")
    print(f"Total images: {len(image_data)}")
    print(f"Successfully downloaded: {len(downloaded)}")
    print(f"Errors: {len(errors)}")
    
    if errors:
        print("\n=== Errors ===")
        for error in errors:
            print(error)

if __name__ == "__main__":
    main()
