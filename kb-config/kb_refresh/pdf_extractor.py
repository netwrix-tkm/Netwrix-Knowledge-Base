"""
Simplified PDF Extraction Module

This module extracts clean plain text from PDF files, removing special characters and boilerplate content.
"""

import os
import re
import unicodedata
from typing import Optional, List, Set


class PDFExtractor:
    """PDF text extraction class that produces clean plain text."""

    def __init__(self, output_dir: Optional[str] = None):
        """
        Initialize the PDF extractor.

        Args:
            output_dir: Directory to save extracted text files. If None, text files will be saved 
                       in the same directory as the PDF files.
        """
        self.output_dir = output_dir
        
        # Try to import required libraries
        try:
            import PyPDF2
            self.pdf_library = "pypdf2"
            self.PyPDF2 = PyPDF2
            print("Using PyPDF2 for PDF extraction")
        except ImportError:
            try:
                import pdfplumber
                self.pdf_library = "pdfplumber"
                self.pdfplumber = pdfplumber
                print("Using pdfplumber for PDF extraction")
            except ImportError:
                raise ImportError("Neither PyPDF2 nor pdfplumber is installed. "
                                 "Install with 'pip install PyPDF2' or 'pip install pdfplumber'")

    def extract_text(self, pdf_path: str) -> str:
        """
        Extract text from a PDF file.
        
        Args:
            pdf_path: Path to the PDF file.
            
        Returns:
            Clean, extracted text content.
        """
        print(f"Extracting text from {pdf_path}")

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        raw_text = ""
        
        try:
            if self.pdf_library == "pypdf2":
                raw_text = self._extract_with_pypdf2(pdf_path)
                else:
                raw_text = self._extract_with_pdfplumber(pdf_path)
                
            # Clean the text
            clean_text = self._clean_text(raw_text, os.path.basename(pdf_path))
            
            return clean_text
                
        except Exception as e:
            error_msg = f"Error extracting text from {pdf_path}: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)
            
    def _extract_with_pypdf2(self, pdf_path: str) -> str:
        """Extract text using PyPDF2."""
        with open(pdf_path, 'rb') as file:
            reader = self.PyPDF2.PdfReader(file)
            total_pages = len(reader.pages)
            print(f"PDF has {total_pages} pages")
            
            # Skip first few pages (usually cover, TOC, etc.) and last few pages (usually appendix, index)
            # Only if the PDF is long enough
            start_page = min(3, max(0, total_pages // 10)) if total_pages > 10 else 0
            end_page = max(0, total_pages - 2) if total_pages > 10 else total_pages
            
            print(f"Extracting content from pages {start_page + 1} to {end_page}")
            
            all_text = []
            for page_num in range(start_page, end_page):
                if page_num % 10 == 0:
                    print(f"Processing page {page_num + 1}/{total_pages}")
                try:
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    if text:
                        all_text.append(text)
                except Exception as e:
                    print(f"Warning: Could not extract text from page {page_num + 1}: {e}")
            
            return "\n".join(all_text)
            
    def _extract_with_pdfplumber(self, pdf_path: str) -> str:
        """Extract text using pdfplumber."""
        with self.pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"PDF has {total_pages} pages")
            
            # Skip first few pages (usually cover, TOC, etc.) and last few pages (usually appendix, index)
            # Only if the PDF is long enough
            start_page = min(3, max(0, total_pages // 10)) if total_pages > 10 else 0
            end_page = max(0, total_pages - 2) if total_pages > 10 else total_pages
            
            print(f"Extracting content from pages {start_page + 1} to {end_page}")
            
            all_text = []
            for page_num in range(start_page, end_page):
                if page_num % 10 == 0:
                    print(f"Processing page {page_num + 1}/{total_pages}")
                try:
                    page = pdf.pages[page_num]
                    text = page.extract_text()
                    if text:
                        all_text.append(text)
                except Exception as e:
                    print(f"Warning: Could not extract text from page {page_num + 1}: {e}")
            
            return "\n".join(all_text)
    
    def _clean_text(self, text: str, filename: str) -> str:
        """
        Clean and normalize extracted text, removing boilerplate content,
        special characters and formatting.
        
        Args:
            text: Raw text to clean
            filename: PDF filename to extract product name for removal
            
        Returns:
            Cleaned text
        """
        if not text:
            return ""
            
        # Extract product name from filename to help with removing boilerplate
        product_name = os.path.splitext(filename)[0]
        product_name = re.sub(r'[_-]', ' ', product_name)
        
        # Get common words from product name for detection
        name_parts = set(word.lower() for word in product_name.split() if len(word) > 3)
        
        # Patterns to remove
        patterns_to_remove = [
            # Copyright notices
            r'Copyright\s+\d{4}.*?reserved',
            r'©\s*\d{4}.*?reserved',
            r'All\s+rights\s+reserved',
            
            # Headers and footers
            r'^.{0,30}page\s+\d+\s+of\s+\d+.{0,30}$',
            r'^\s*\d+\s*$',  # Just page numbers
            
            # Table of contents patterns
            r'^Table\s+of\s+contents$',
            r'^\s*Contents\s*$',
            r'^.*\.\.\.\.\.\s*\d+$',  # TOC lines with page numbers
            
            # Common document sections to skip
            r'^Legal\s+Information$',
            r'^Disclaimer$',
            r'^Index$',
            r'^Appendix$',
        ]
        
        # Replace special characters
        special_chars = {
            '\u2022': ' ',        # Bullet point
            '\u25e6': ' ',        # White bullet
            '\u2013': '-',        # En dash
            '\u2014': '-',        # Em dash
            '\u201c': '"',        # Left double quote
            '\u201d': '"',        # Right double quote
            '\u2018': "'",        # Left single quote
            '\u2019': "'",        # Right single quote
            '\u00a0': ' ',        # Non-breaking space
            '\u00ad': '',         # Soft hyphen
            '\u200b': '',         # Zero width space
        }
        
        for char, replacement in special_chars.items():
            text = text.replace(char, replacement)
        
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Split into lines for easier processing
                    lines = text.split('\n')
        clean_lines = []
        
                    for line in lines:
                        line = line.strip()
                        if not line:
                            continue
                        
            # Skip if line looks like boilerplate
            skip_line = False
            
            # Skip lines that match patterns to remove
            for pattern in patterns_to_remove:
                if re.search(pattern, line, re.IGNORECASE):
                    skip_line = True
                                break
                                
            # Skip lines that contain too many words from product name (likely headers/footers)
            line_words = set(word.lower() for word in line.split() if len(word) > 3)
            if len(line_words.intersection(name_parts)) >= 3 and len(line) < 100:
                skip_line = True
            
            # Skip very short lines likely to be page artifacts
            if len(line) < 5:
                skip_line = True
                
            if not skip_line:
                clean_lines.append(line)
        
        # Join lines back together with single spaces
        clean_text = ' '.join(clean_lines)
        
        # Fix hyphenated words
        clean_text = re.sub(r'(\w)- (\w)', r'\1\2', clean_text)
        
        # Fix spacing in common patterns
        clean_text = re.sub(r'(\w): (\w)', r'\1: \2', clean_text)  # Fix spacing after colons
        
        # Replace multiple spaces with single space
        clean_text = re.sub(r' +', ' ', clean_text)
                
        # Remove duplicate sentences (common with some PDF extractors)
        sentences = []
        for sentence in re.split(r'(?<=[.!?])\s+', clean_text):
            if sentence and sentence not in sentences[-3:]:  # Check if in last 3 sentences
                sentences.append(sentence)
                
        clean_text = ' '.join(sentences)
        
        # Filter out any non-printable characters
        clean_text = ''.join(ch for ch in clean_text if unicodedata.category(ch)[0] != 'C')
            
        return clean_text.strip()

    def extract_and_save(self, pdf_path: str) -> str:
        """
        Extract clean text from a PDF file and save it to a plain text file.
        
        Args:
            pdf_path: Path to the PDF file.
            
        Returns:
            Path to the saved text file.
        """
        # Extract the text
        text = self.extract_text(pdf_path)
        
        # Determine the output file path
        if self.output_dir:
            os.makedirs(self.output_dir, exist_ok=True)
            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            output_file = os.path.join(self.output_dir, f"{base_name}.txt")
        else:
            output_file = os.path.splitext(pdf_path)[0] + ".txt"
        
        # Save the text to a file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f"Clean text extracted and saved to {output_file}")
        return output_file

    # For backwards compatibility with existing code
    def extract_text_with_sections(self, pdf_path: str) -> dict:
        """
        Legacy method for backwards compatibility. 
        Now just returns a simplified structure with all text in a single section.
        """
        text = self.extract_text(pdf_path)
        product_name = os.path.splitext(os.path.basename(pdf_path))[0]
        
        result = {
            "metadata": {
                "product_name": product_name,
                "source_file": os.path.basename(pdf_path),
                "extractor": self.pdf_library,
            },
            "sections": [
                {
                    "section_name": "Full Document",
                    "text": text,
                    "page_range": [1],  # Simplified placeholder
                    "level": 1,
                    "parent_section": None
                }
            ]
        }
        return result


def extract_pdf_to_text(pdf_path: str, output_dir: Optional[str] = None) -> str:
        """
    Helper function to extract clean text from a PDF file and save it to a plain text file.
        
        Args:
        pdf_path: Path to the PDF file.
        output_dir: Directory to save the text file. If None, the text file will be 
                   saved in the same directory as the PDF file.
            
        Returns:
        Path to the saved text file.
    """
    extractor = PDFExtractor(output_dir)
    return extractor.extract_and_save(pdf_path)


# For backwards compatibility with existing code
def get_extractor(backend: str = "pypdf2", **kwargs) -> PDFExtractor:
    """
    Get a PDF extractor instance (for backwards compatibility).

    Args:
        backend: Name of backend (ignored in this simplified version)
        **kwargs: Additional arguments (passed to PDFExtractor)

    Returns:
        A PDFExtractor instance
    """
    output_dir = kwargs.get('output_dir')
    return PDFExtractor(output_dir=output_dir)
