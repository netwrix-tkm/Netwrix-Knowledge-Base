"""
Text Embedding Module

This module handles the generation of embeddings for document chunks.
"""

import json
import os
from typing import Dict, List, Optional, Union

import numpy as np


class TextEmbedder:
    """Handles the generation of embeddings for document chunks."""

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
        device: str = "cpu",
        output_dir: str = "embeddings",
    ):
        """
        Initialize the text embedder.

        Args:
            model_name: Name of the sentence-transformer model to use.
            device: Device to use for embedding generation ("cpu" or "cuda").
            output_dir: Directory to save embeddings to.
        """
        self.model_name = model_name
        self.device = device
        self.output_dir = output_dir
        
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(model_name, device=device)
        except ImportError:
            raise ImportError(
                "sentence-transformers not installed. "
                "Install with 'pip install sentence-transformers'"
            )
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

    def generate_embeddings(self, chunked_document: Dict) -> Dict:
        """
        Generate embeddings for document chunks.

        Args:
            chunked_document: A dictionary with chunks from the document chunker.

        Returns:
            The document with embeddings added to each chunk.
        """
        product_name = chunked_document.get("product_name", "Unknown")
        chunks = chunked_document.get("chunks", [])
        
        texts = [chunk["text"] for chunk in chunks]
        
        # Generate embeddings in batches
        embeddings = self.model.encode(texts)
        
        # Add embeddings to chunks
        for i, chunk in enumerate(chunks):
            chunk["embedding"] = embeddings[i].tolist()
            
        return chunked_document
    
    def save_embeddings(self, embedded_document: Dict, filename: Optional[str] = None) -> str:
        """
        Save document embeddings to a jsonl file.

        Args:
            embedded_document: A dictionary with embedded document chunks.
            filename: Optional filename to save embeddings to.

        Returns:
            Path to the saved embeddings file.
        """
        product_name = embedded_document.get("product_name", "Unknown")
        filename = filename or f"{product_name}_embeddings.jsonl"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            for chunk in embedded_document.get("chunks", []):
                f.write(json.dumps(chunk) + "\n")
                
        return filepath
    
    def load_embeddings(self, filepath: str) -> Dict:
        """
        Load document embeddings from a jsonl file.

        Args:
            filepath: Path to the embeddings file.

        Returns:
            A dictionary with product name and embedded chunks.
        """
        chunks = []
        product_name = os.path.splitext(os.path.basename(filepath))[0].replace("_embeddings", "")
        
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                chunks.append(json.loads(line))
                
        return {
            "product_name": product_name,
            "chunks": chunks
        }
        
    def compute_similarity(
        self, 
        query_embedding: List[float], 
        doc_embeddings: List[List[float]]
    ) -> List[float]:
        """
        Compute cosine similarity between query and document embeddings.

        Args:
            query_embedding: Embedding vector for the query.
            doc_embeddings: List of embedding vectors for documents.

        Returns:
            List of similarity scores.
        """
        query_embedding = np.array(query_embedding)
        doc_embeddings = np.array(doc_embeddings)
        
        # Normalize embeddings for cosine similarity
        query_norm = np.linalg.norm(query_embedding)
        if query_norm > 0:
            query_embedding = query_embedding / query_norm
            
        doc_norms = np.linalg.norm(doc_embeddings, axis=1, keepdims=True)
        doc_norms[doc_norms == 0] = 1  # Avoid division by zero
        doc_embeddings = doc_embeddings / doc_norms
        
        # Compute cosine similarity
        similarities = np.dot(doc_embeddings, query_embedding)
        
        return similarities.tolist() 