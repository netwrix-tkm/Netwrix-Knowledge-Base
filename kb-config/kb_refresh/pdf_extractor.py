"""
PDF Text Extractor using pdfplumber

This module provides functionality to extract and clean text from PDF files while
preserving document structure, tables, and formatting.
"""

import os
import re
import logging
import pdfplumber
from typing import List, Dict, Optional, Tuple, Union
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add path handling for directories
# Get the base project directory (2 levels up from this script)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

# Common page headers/footers to remove
COMMON_HEADERS = [
    # Page numbers and document info
    r'\b(?:page|pg\.?)\s*\d+\b',
    r'\b\d+\s+of\s+\d+\b',
    r'\b\d{1,2}/\d{1,2}/\d{2,4}\b',
    r'\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+\d{1,2},?\s+\d{4}\b',
    r'©|©|\[?\s*confidential\s*\]?',
    r'document\s+\w+\s+\d+',
    r'\bversion\s+\d+(\.\d+)*\b',
    
    # Common footer patterns
    r'(?i)\b(?:confidential|proprietary|internal use only|do not distribute)\b',
    r'(?i)\b(?:draft|preliminary|unclassified|for review)\b',
    
    # Document identifiers
    r'(?i)\b(?:doc|document|ref|reference|rev|revision)\s*[#:]?\s*[a-z0-9-]+\b',
    
    # Common legal text
    r'(?i)\b(?:all rights reserved|confidential information|proprietary and confidential)\b',
    
    # Common section headers that might appear as footers
    r'(?i)\b(?:appendix|annex|attachments?|references?|notes?|footnotes?|endnotes?)\s*[a-z0-9]*\s*$'
]

# Common section headers
SECTION_HEADERS = [
    r'^\s*\d+(\.\d+)*\s+[A-Z][A-Za-z0-9\s]+$',  # 1.1 Section Title
    r'^\s*[A-Z][A-Z0-9\s]+$',  # ALL CAPS HEADER
    r'^\s*[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*$',  # Title Case Header
]

def is_section_header(text: str) -> bool:
    """Check if text appears to be a section header."""
    text = text.strip()
    if not text or len(text) > 100:  # Too long to be a header
        return False
    return any(re.match(pattern, text, re.IGNORECASE) for pattern in SECTION_HEADERS)

class PDFExtractor:
    """Extracts and processes text from PDF files using pdfplumber."""
    
    def __init__(self, x_tolerance: int = 3, y_tolerance: int = 3):
        """
        Initialize the PDF extractor.
        
        Args:
            x_tolerance: Horizontal tolerance for text extraction
            y_tolerance: Vertical tolerance for text extraction
        """
        self.x_tolerance = x_tolerance
        self.y_tolerance = y_tolerance
        self.current_section = None
        self.in_table = False
        self.table_lines = []
        
    def _clean_text(self, text: str) -> str:
        """
        Clean and normalize extracted text, removing footers and bullet points.
        
        Args:
            text: Raw extracted text
            
        Returns:
            Cleaned and normalized text
        """
        if not text or not text.strip():
            return ""
            
        # Remove common headers/footers first
        for pattern in COMMON_HEADERS:
            text = re.sub(pattern, '', text, flags=re.IGNORECASE)
            
        # Remove copyright notices with various formats
        text = re.sub(
            r'(?i)(?:©|©|copyright\s+)?\s*(?:\d{4}\s*,\s*)*(?:\d{4})\s*' 
            r'(?:netwrix|all rights reserved|privilege secure)[\s\S]*?$',
            '', text
        )
        
        # Remove product name footers with version numbers
        text = re.sub(
            r'(?i)(?:netwrix\s+)?(?:privilege\s+secure|pam|sbam)[\s\S]*?'
            r'(?:v?\d+(?:\.\d+)+)?(?:\s*\([^)]*\))?\s*$',
            '', text
        )
        
        # Remove page number footers
        text = re.sub(r'(?i)\b(?:page|pg\.?)\s*\d+\s*(?:of\s*\d+)?\s*$', '', text)
        
        # Remove all bullet points (•, ▪, ♦, -, *, etc.) at start of line
        text = re.sub(r'^\s*[•▪♦\-*]\s*', '', text, flags=re.MULTILINE)
        
        # Remove any remaining bullet points in the middle of text
        text = re.sub(r'\s*[•▪♦]\s*', ' ', text)
        
        # Normalize all whitespace
        text = ' '.join(text.split())
        
        return text.strip()
        
    def _extract_table(self, table: List[List[str]]) -> str:
        """
        Format an extracted table as text.
        
        Args:
            table: 2D list of table cells
            
        Returns:
            Formatted table as a string
        """
        if not table or not any(table):
            return ""
            
        # Determine column widths
        col_widths = [max(len(str(cell)) for cell in col) 
                     for col in zip(*table)]
        
        # Build table rows
        rows = []
        for row in table:
            row_str = "| " + " | ".join(
                str(cell).ljust(width) 
                for cell, width in zip(row, col_widths)
            ) + " |"
            rows.append(row_str)
            
        # Add header separator
        if rows:
            sep = "+-" + "-+-".join(["-" * w for w in col_widths]) + "-+" 
            rows.insert(1, sep)
            
        return "\n".join(rows)
        
    def _is_header_or_footer(self, text: str, page_num: int, total_pages: int) -> bool:
        """Check if text appears to be a header or footer."""
        text = text.strip().lower()
        
        # Check for page numbers
        if text == str(page_num) or text == f"{page_num} of {total_pages}":
            return True
            
        # Check for common header/footer patterns
        if any(re.search(pattern, text) for pattern in [
            r'^\s*\d+\s*$',  # Just a number
            r'^\s*[ivxlc]+\s*$',  # Roman numerals
            r'^\s*\d{1,2}/\d{1,2}/\d{2,4}\s*$',  # Dates
            r'^\s*[a-z]\s*$',  # Single letters
            r'^\s*confidential\s*$',
            r'^\s*draft\s*$',
            r'^\s*page\s+\d+\s*$',
        ]):
            return True
            
        return False
    
    def extract_text(self, pdf_path: str) -> str:
        """
        Extract text from a PDF file with improved formatting and cleanup.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Cleaned and formatted text as a string
            
        Raises:
            FileNotFoundError: If the PDF file is not found
            pdfplumber.PDFSyntaxError: If there's an error reading the PDF
            Exception: For any other errors during PDF processing
        """
        try:
            all_text = []
            with pdfplumber.open(pdf_path) as pdf:
                logger.info(f"Processing PDF with {len(pdf.pages)} pages")
                
                for i, page in enumerate(pdf.pages):
                    try:
                        page_text = []
                        
                        # Extract tables first
                        table_text = self._extract_tables(page)
                        if table_text:
                            page_text.append(table_text)
                        
                        # Extract regular text
                        text = page.extract_text(
                            x_tolerance=self.x_tolerance,
                            y_tolerance=self.y_tolerance,
                            layout=True
                        )
                        
                        if text:
                            # Clean up the text
                            lines = []
                            for line in text.split('\n'):
                                line = line.strip()
                                if not line:
                                    continue
                                    
                                # Skip common footer/header elements
                                if (re.match(r'^\s*\d+\s*$', line) or  # Just a number (page number)
                                    re.search(r'(?i)page\s+\d+', line) or  # "Page X"
                                    re.search(r'(?i)copyright', line) or
                                    re.search(r'(?i)all rights reserved', line)):
                                    continue
                                    
                                # Remove product name and version from the beginning of the line
                                line = re.sub(r'^.*?(v\d+(?:\.\d+){1,2})', r'\1', line, flags=re.IGNORECASE)
                                
                                # Clean up the line
                                line = re.sub(r'^[•▪♦\-*]\s*', '', line)  # Remove bullet points
                                line = re.sub(r'\s*[•▪♦]\s*', ' ', line)   # Remove other bullet points
                                line = re.sub(r'\s+', ' ', line).strip()    # Normalize whitespace
                                
                                if line:  # Only add non-empty lines
                                    lines.append(line)
                            
                            if lines:
                                page_text.append(' '.join(lines))
                        
                        if page_text:
                            all_text.append('\n'.join(page_text))
                            
                    except Exception as e:
                        logger.warning(f"Error processing page {i+1}: {str(e)}")
                        continue
            
            if not all_text:
                logger.warning("No text was extracted from the PDF")
                return ""
                
            # Join all pages with double newlines
            full_text = '\n\n'.join(all_text)
            
            # Clean up any remaining artifacts
            full_text = re.sub(r'\s+', ' ', full_text)  # Normalize all whitespace
            full_text = re.sub(r'(\w)-\s+(\w)', r'\1\2', full_text)  # Fix hyphenated words
            
            return full_text.strip()
            
                
        except Exception as e:
            logger.error(f"Error processing {pdf_path}: {str(e)}")
            raise
    
    def _clean_text(self, text: str) -> str:
        """Clean and normalize extracted text."""
        if not text:
            return ""
            
        # Split into lines and process each line
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Remove everything before version pattern (vX.Y or vX.Y.Z)
            line = re.sub(r'^.*?(v\d+(?:\.\d+){1,2})', r'\1', line, flags=re.IGNORECASE)
            cleaned_lines.append(line.strip())
        
        # Join lines with newlines and normalize whitespace
        text = '\n'.join(cleaned_lines)
        text = re.sub(r'\s+', ' ', text)  # Normalize whitespace within each line
        
        # Fix common PDF artifacts
        text = re.sub(r'(\w)-\s+(\w)', r'\1\2', text)  # Fix hyphenated words
        
        return text.strip()
    
    def _extract_tables(self, page) -> str:
        """Extract and format tables from a page."""
        tables = page.extract_tables()
        if not tables:
            return ""
            
        table_texts = []
        
        for i, table in enumerate(tables, 1):
            if not table or not any(any(cell for cell in row) for row in table):
                continue
                
            # Calculate column widths
            col_widths = []
            for col in zip(*table):
                max_width = max(len(str(cell or '')) for cell in col)
                col_widths.append(max_width + 2)  # Add padding
            
            # Format table
            table_lines = [f"\nTable {i}:"]
            
            for row in table:
                if not any(cell for cell in row):
                    continue
                    
                # Format each row
                formatted_row = []
                for cell, width in zip(row, col_widths):
                    cell_str = str(cell or '').strip()
                    formatted_row.append(cell_str.ljust(width))
                
                table_lines.append(' '.join(formatted_row).rstrip())
            
            table_texts.append('\n'.join(table_lines))
        
        return '\n\n'.join(table_texts)
    
    def _post_process(self, text: str) -> str:
        """Apply final formatting and cleanup to the extracted text."""
        if not text:
            return ""
            
        # Fix common formatting issues
        text = re.sub(r'\n{3,}', '\n\n', text)  # Remove excessive newlines
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # Add space between lower and uppercase
        text = re.sub(r'([.!?])([A-Z])', r'\1 \\n\\n\2', text)  # Add newlines after sentences
        
        # Fix common technical terms
        text = re.sub(r'\\b([A-Z])([A-Z]+)\\b', 
                     lambda m: m.group(1) + m.group(2).lower(), 
                     text)
        
        return text.strip()

def process_pdf_file(input_path: str, output_dir: str) -> str:
    """
    Process a single PDF file and save the extracted text.
    
    Args:
        input_path: Path to the input PDF file
        output_dir: Directory to save the extracted text
        
    Returns:
        Path to the output text file
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate output filename
        filename = os.path.basename(input_path)
        output_filename = f"{os.path.splitext(filename)[0]}_extracted.txt"
        output_path = os.path.join(output_dir, output_filename)
        
        # Extract text
        extractor = PDFExtractor()
        extracted_text = extractor.extract_text(input_path)
        
        # Save to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(extracted_text)
        
        logger.info(f"Successfully processed {filename} -> {output_path}")
        return output_path
        
    except Exception as e:
        logger.error(f"Error processing {input_path}: {str(e)}")
        raise

def process_directory(input_dir: str, output_dir: str) -> None:
    """
    Process all PDF files in a directory.
    
    Args:
        input_dir: Directory containing PDF files
        output_dir: Directory to save extracted text files
    """
    if not os.path.isdir(input_dir):
        raise ValueError(f"Input directory does not exist: {input_dir}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each PDF file
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(input_dir, filename)
            try:
                process_pdf_file(input_path, output_dir)
            except Exception as e:
                logger.error(f"Failed to process {filename}: {str(e)}")

def extract_pdf_to_text(pdf_path: str, output_dir: str = None, **kwargs) -> str:
    """
    Extract text from a PDF file and save it to a text file in the specified directory.
    
    Args:
        pdf_path: Path to the input PDF file
        output_dir: Directory to save the extracted text file
        **kwargs: Additional arguments (ignored)
        
    Returns:
        Path to the saved text file
    """
    try:
        # Create output directory if it doesn't exist
        if output_dir is None:
            output_dir = os.path.join(BASE_DIR, "kb-config", "kb_refresh", "extracted")
        
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate output filename based on input PDF filename
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_path = os.path.join(output_dir, f"{base_name}_extracted.txt")
        
        # Extract text using PDFExtractor
        extractor = PDFExtractor()
        text = extractor.extract_text(pdf_path)
        
        # Save to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        logger.info(f"Extracted text saved to: {output_path}")
        return output_path
        
    except Exception as e:
        logger.error(f"Error extracting text from {pdf_path}: {str(e)}")
        raise


def get_extractor(backend: str = 'pdfplumber'):
    """
    Get an instance of the PDF extractor with the specified backend.
    
    Args:
        backend: The backend to use for PDF extraction (default: 'pdfplumber')
                Note: Currently, only 'pdfplumber' backend is supported.
                
    Returns:
        An instance of PDFExtractor
        
    Raises:
        ValueError: If an unsupported backend is specified
    """
    if backend != 'pdfplumber':
        logger.warning(f"Backend '{backend}' not supported. Using 'pdfplumber' instead.")
    
    return PDFExtractor()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Extract text from PDF files')
    parser.add_argument('input', help='Input PDF file or directory')
    parser.add_argument('-o', '--output', help='Output directory', default='extracted')
    
    args = parser.parse_args()
    
    if os.path.isfile(args.input):
        process_pdf_file(args.input, args.output)
    elif os.path.isdir(args.input):
        process_directory(args.input, args.output)
    else:
        print(f"Error: {args.input} is not a valid file or directory")
        exit(1)