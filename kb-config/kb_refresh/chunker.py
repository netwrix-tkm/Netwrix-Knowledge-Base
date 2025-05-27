"""
Document Chunking Module

This module handles the chunking of document text based on section headings.
"""

from typing import Dict, List, Optional, Union


class DocumentChunker:
    """Handles the chunking of document text based on section headings."""

    def __init__(
        self,
        max_chunk_size: int = 1000,
        min_chunk_size: int = 100,
        overlap: int = 50
    ):
        """
        Initialize the document chunker.

        Args:
            max_chunk_size: Maximum number of characters in a chunk.
            min_chunk_size: Minimum number of characters in a chunk.
            overlap: Number of characters to overlap between chunks.
        """
        self.max_chunk_size = max_chunk_size
        self.min_chunk_size = min_chunk_size
        self.overlap = overlap

    def chunk_document(
        self, 
        document: Dict[str, List[Dict[str, Union[str, int, List[int]]]]]
    ) -> Dict[str, List[Dict]]:
        """
        Chunk a document into smaller text chunks based on section headings.

        Args:
            document: A dictionary with document sections from the PDF extractor.

        Returns:
            A dictionary with product name and chunked sections.
        """
        product_name = document.get("product_name", "Unknown")
        sections = document.get("sections", [])
        
        chunked_sections = []
        chunk_id = 0
        
        for section in sections:
            section_name = section.get("section_name", "Unknown Section")
            text = section.get("text", "")
            page_range = section.get("page_range", [])
            parent_section = section.get("parent_section")
            level = section.get("level", 1)
            
            # Create chunks from this section's text
            if not text:
                continue
                
            # If the section is small enough, keep it as a single chunk
            if len(text) <= self.max_chunk_size:
                chunked_sections.append({
                    "chunk_id": f"{product_name}_{chunk_id}",
                    "section_name": section_name,
                    "parent_section": parent_section,
                    "level": level,
                    "text": text,
                    "page_range": page_range
                })
                chunk_id += 1
                continue
            
            # Otherwise, split into multiple chunks
            chunks = self._split_text_into_chunks(text)
            
            for i, chunk_text in enumerate(chunks):
                chunked_sections.append({
                    "chunk_id": f"{product_name}_{chunk_id}",
                    "section_name": section_name,
                    "parent_section": parent_section,
                    "level": level,
                    "text": chunk_text,
                    "page_range": page_range,
                    "chunk_index": i,
                    "total_chunks": len(chunks)
                })
                chunk_id += 1
                
        return {
            "product_name": product_name,
            "chunks": chunked_sections
        }
        
    def _split_text_into_chunks(self, text: str) -> List[str]:
        """
        Split text into chunks of maximum size with overlap.
        
        Args:
            text: The text to split.
            
        Returns:
            A list of text chunks.
        """
        if len(text) <= self.max_chunk_size:
            return [text]
            
        chunks = []
        start = 0
        
        while start < len(text):
            # Find a good breaking point (end of a sentence or paragraph)
            end = start + self.max_chunk_size
            if end >= len(text):
                chunks.append(text[start:])
                break
                
            # Try to find a period or newline to break at
            break_point = self._find_break_point(text, start, end)
            
            # Add the chunk
            chunks.append(text[start:break_point])
            
            # Move start position for next chunk, considering overlap
            start = break_point - self.overlap
            if start < 0:
                start = 0
        
        # Ensure minimum chunk size
        return [chunk for chunk in chunks if len(chunk) >= self.min_chunk_size]
    
    def _find_break_point(self, text: str, start: int, end: int) -> int:
        """Find a good breaking point for text chunking."""
        # Try to find a paragraph break first
        for i in range(end, start, -1):
            if i < len(text) and text[i-1:i+1] == '\n\n':
                return i + 1
        
        # Try to find a sentence break
        for i in range(end, start, -1):
            if i < len(text) and text[i-1:i+1] in ['. ', '.\n']:
                return i + 1
                
        # If no good break point found, just break at max_chunk_size
        return end 