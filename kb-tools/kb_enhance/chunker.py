"""
Document Chunking Module

This module handles the chunking of document text into sentences.
"""

import nltk
from typing import Dict, List, Optional, Union

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('perluniprops')
    nltk.download('universal_tagset')

from nltk.tokenize import sent_tokenize


class DocumentChunker:
    """Handles the chunking of document text based on section headings."""

    def __init__(
        self,
        max_chunk_size: int = 1000,
        min_chunk_size: int = 100,
        overlap: int = 50,
        sentences_per_chunk: int = 4,
        overlap_sentences: int = 1
    ):
        """
        Initialize the document chunker.

        Args:
            max_chunk_size: Maximum number of characters in a chunk.
            min_chunk_size: Minimum number of characters in a chunk.
            overlap: Number of characters to overlap between chunks.
            sentences_per_chunk: Number of sentences to include in each chunk.
            overlap_sentences: Number of sentences to overlap between chunks.
        """
        self.max_chunk_size = max_chunk_size
        self.min_chunk_size = min_chunk_size
        self.overlap = overlap
        self.sentences_per_chunk = sentences_per_chunk
        self.overlap_sentences = overlap_sentences

    def chunk_document(
        self, 
        document: Dict[str, List[Dict[str, Union[str, int, List[int]]]]]
    ) -> Dict[str, List[Dict]]:
        """
        Chunk a document into smaller text chunks.

        Args:
            document: A dictionary with document sections from the PDF extractor.

        Returns:
            A dictionary with product name and chunked text.
        """
        product_name = document.get("product_name", "Unknown")
        sections = document.get("sections", [])
        
        # Combine all sections into a single text
        full_text = ""
        for section in sections:
            text = section.get("text", "").strip()
            if text:
                full_text += " " + text
        full_text = full_text.strip()
        
        # Split into chunks
        chunks = self._split_text_into_chunks(full_text)
        
        # Format chunks
        chunked_sections = [
            {
                "chunk_id": f"{product_name}_{i}",
                "text": chunk,
                "chunk_index": i,
                "total_chunks": len(chunks)
            }
            for i, chunk in enumerate(chunks)
        ]
                
        return {
            "product_name": product_name,
            "chunks": chunked_sections
        }
        
    def _split_text_into_chunks(self, text: str) -> List[str]:
        """
        Split text into chunks of multiple sentences with overlap.
        
        Args:
            text: The text to split into chunks.
            
        Returns:
            A list of text chunks.
        """
        if not text or len(text.strip()) == 0:
            return []
            
        # Split text into sentences using NLTK
        sentences = sent_tokenize(text)
        
        # Filter out very short sentences (likely artifacts)
        valid_sentences = [s.strip() for s in sentences if len(s.strip()) >= 5]  # Using a smaller threshold for individual sentences
        
        if not valid_sentences:
            return []
        
        chunks = []
        i = 0
        
        # Create chunks with specified number of sentences and overlap
        while i < len(valid_sentences):
            # Get sentences for this chunk
            end_idx = min(i + self.sentences_per_chunk, len(valid_sentences))
            chunk_sentences = valid_sentences[i:end_idx]
            
            # Join sentences into a single text chunk
            chunk = " ".join(chunk_sentences)
            
            # Only add chunks that meet the minimum size requirement
            if len(chunk) >= self.min_chunk_size:
                chunks.append(chunk)
            
            # Move index forward, accounting for overlap
            i += max(1, self.sentences_per_chunk - self.overlap_sentences)
        
        return chunks
    
    def _find_break_point(self, text: str, start: int, end: int) -> int:
        """
        This method is kept for backward compatibility but is not used
        when splitting by sentences.
        """
        return end