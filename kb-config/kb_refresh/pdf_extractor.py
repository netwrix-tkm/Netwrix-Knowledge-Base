"""
Simple PDF Extraction Module

This module extracts plain text from PDF files, removing special characters and boilerplate content.
"""

import os
import re
import unicodedata
from typing import Optional


def clean_text(text):
    """Clean and normalize extracted text, removing special characters and boilerplate content."""
    if not text:
        return ""
    
    # Replace unicode chars with ASCII equivalents or spaces
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    # Replace multiple whitespace with single space
    text = re.sub(r'\s+', ' ', text)
    
    # Remove common boilerplate patterns
    patterns_to_remove = [
        r'copyright \d{4}.*?reserved',
        r'all rights reserved',
        r'page \d+ of \d+',
        r'^\s*\d+\s*$',  # Just page numbers
        r'table of contents',
        r'netwrix',
        r'privilege secure',
    ]
    
    for pattern in patterns_to_remove:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    
    # Fix hyphenated words
    text = re.sub(r'(\w)- (\w)', r'\1\2', text)
    
    # Final cleanup
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_pdf_to_text(pdf_path, output_dir=None):
    """
    Extract text from a PDF file and save as plain text.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save the text file (optional)
        
    Returns:
        Path to the saved text file
    """
    print(f"Extracting text from {pdf_path}")
    
    # Try importing PDF extraction libraries
    try:
        import PyPDF2
        use_pypdf2 = True
        print("Using PyPDF2")
    except ImportError:
        try:
            import pdfplumber
            use_pypdf2 = False
            print("Using pdfplumber")
        except ImportError:
            raise ImportError("Neither PyPDF2 nor pdfplumber installed. Please install one.")
    
    # Ensure the PDF exists
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    # Extract text
    all_text = []
    
    if use_pypdf2:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            total_pages = len(reader.pages)
            print(f"PDF has {total_pages} pages")
            
            # Skip first few pages (cover, TOC) and last page (often copyright)
            start_page = min(2, total_pages // 10) if total_pages > 10 else 0
            end_page = max(0, total_pages - 1) if total_pages > 10 else total_pages
            
            for page_num in range(start_page, end_page):
                if page_num % 10 == 0:
                    print(f"Processing page {page_num + 1}/{total_pages}")
                try:
                    text = reader.pages[page_num].extract_text()
                    if text:
                        all_text.append(text)
                except Exception as e:
                    print(f"Warning: Error extracting page {page_num + 1}: {e}")
    else:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"PDF has {total_pages} pages")
            
            # Skip first few pages and last page
            start_page = min(2, total_pages // 10) if total_pages > 10 else 0
            end_page = max(0, total_pages - 1) if total_pages > 10 else total_pages
            
            for page_num in range(start_page, end_page):
                if page_num % 10 == 0:
                    print(f"Processing page {page_num + 1}/{total_pages}")
                try:
                    text = pdf.pages[page_num].extract_text()
                    if text:
                        all_text.append(text)
                except Exception as e:
                    print(f"Warning: Error extracting page {page_num + 1}: {e}")
    
    # Clean and normalize the text
    raw_text = " ".join(all_text)
    clean_content = clean_text(raw_text)
    
    # Save to output file
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_file = os.path.join(output_dir, f"{base_name}.txt")
    else:
        output_file = os.path.splitext(pdf_path)[0] + ".txt"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(clean_content)
    
    print(f"Text extracted and saved to {output_file}")
    return output_file


# For backwards compatibility
def get_extractor(*args, **kwargs):
    """
    Legacy function for backwards compatibility.
    Instead of returning an extractor object, this returns a simple wrapper.
    """
    class SimpleExtractor:
        def extract_text_with_sections(self, pdf_path):
            text = extract_pdf_text_only(pdf_path)
            return {"text": text}  # Simplified format
            
    return SimpleExtractor()


def extract_pdf_text_only(pdf_path):
    """
    Extract text from PDF without saving to file.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Cleaned text content as string
    """
    # Create a temp file path
    temp_output = extract_pdf_to_text(pdf_path)
    
    # Read the content
    with open(temp_output, 'r', encoding='utf-8') as f:
        content = f.read()
        
    return content
