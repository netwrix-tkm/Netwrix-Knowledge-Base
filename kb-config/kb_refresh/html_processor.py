"""
HTML Processor Module

This module handles the extraction and processing of HTML-based KB articles.
"""

import os
import re
from typing import Dict, List, Optional, Union

from bs4 import BeautifulSoup


class HTMLProcessor:
    """Handles the extraction and processing of HTML-based KB articles."""

    def __init__(self, base_dir: str = "all-articles-html"):
        """
        Initialize the HTML processor.

        Args:
            base_dir: Base directory containing product folders with HTML articles.
        """
        self.base_dir = base_dir

    def get_product_folders(self) -> List[str]:
        """
        Get a list of product folders in the base directory.

        Returns:
            List of product folder names.
        """
        return [
            folder for folder in os.listdir(self.base_dir) 
            if os.path.isdir(os.path.join(self.base_dir, folder))
        ]

    def get_kb_articles(self, product_folder: str) -> List[str]:
        """
        Get a list of KB article files in a product folder.

        Args:
            product_folder: Name of the product folder.

        Returns:
            List of KB article file paths.
        """
        product_path = os.path.join(self.base_dir, product_folder)
        return [
            os.path.join(product_path, file)
            for file in os.listdir(product_path)
            if file.endswith(".html")
        ]

    def extract_kb_article(self, article_path: str) -> Dict[str, str]:
        """
        Extract content from a KB article.

        Args:
            article_path: Path to the KB article file.

        Returns:
            A dictionary with article information.
        """
        try:
            with open(article_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
            
            # Extract title
            title_elem = soup.find("h1") or soup.find("title")
            title = title_elem.text.strip() if title_elem else "Untitled Article"
            
            # Extract body content
            body_elem = soup.find("body") or soup
            
            # Remove script and style elements
            for script in body_elem(["script", "style"]):
                script.decompose()
                
            # Get the text
            body_text = body_elem.get_text(separator="\n").strip()
            
            # Clean up the text (remove excessive newlines, etc.)
            body_text = re.sub(r'\n{3,}', '\n\n', body_text)
            
            article_id = os.path.splitext(os.path.basename(article_path))[0]
            product = os.path.basename(os.path.dirname(article_path))
            
            return {
                "id": article_id,
                "product": product,
                "title": title,
                "content": body_text,
                "path": article_path
            }
            
        except Exception as e:
            print(f"Error extracting content from {article_path}: {e}")
            return {
                "id": os.path.splitext(os.path.basename(article_path))[0],
                "product": os.path.basename(os.path.dirname(article_path)),
                "title": "Error",
                "content": f"Error extracting content: {e}",
                "path": article_path
            }
            
    def save_updated_article(
        self, 
        article: Dict[str, str], 
        updated_content: str,
        output_folder: str = "updated_articles"
    ) -> str:
        """
        Save an updated KB article.

        Args:
            article: The original KB article dictionary.
            updated_content: The updated content.
            output_folder: Folder to save updated articles to.

        Returns:
            Path to the saved article.
        """
        product = article["product"]
        article_id = article["id"]
        
        # Create output directories
        output_path = os.path.join(self.base_dir, product, output_folder)
        os.makedirs(output_path, exist_ok=True)
        
        output_file = os.path.join(output_path, f"{article_id}.html")
        
        try:
            with open(article["path"], "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
                
            # Find the main content element (this may need customization based on the HTML structure)
            content_elem = soup.find("div", class_="article-body") or soup.find("body")
            
            if content_elem:
                # Replace the content
                content_elem.clear()
                content_elem.append(BeautifulSoup(updated_content, "html.parser"))
                
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(str(soup))
            else:
                # If we can't find a proper container, create a simple HTML file
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(f"<html><head><title>{article['title']}</title></head>")
                    f.write(f"<body>{updated_content}</body></html>")
                    
            return output_file
            
        except Exception as e:
            print(f"Error saving updated article {article_id}: {e}")
            
            # Create a simple error file
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"<html><head><title>Error: {article['title']}</title></head>")
                f.write(f"<body><h1>Error Updating Article</h1><p>{e}</p></body></html>")
                
            return output_file 