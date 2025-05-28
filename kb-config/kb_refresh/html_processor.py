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
        Extract and clean content from a KB article.

        Args:
            article_path: Path to the KB article file.

        Returns:
            A dictionary with article information containing cleaned content.
        """
        try:
            with open(article_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
            
            # Extract title from h1 or title tag
            title_elem = soup.find("h1") or soup.find("title")
            title = title_elem.get_text(strip=True) if title_elem else "Untitled Article"
            
            # Find the main content area - look for common content containers
            content_selectors = [
                "article",  # HTML5 article tag
                "div.article-body",  # Common class for article content
                "div.content",
                "div.main-content",
                "div#content",
                "main"  # HTML5 main tag
            ]
            
            # Try to find the main content container
            content_elem = None
            for selector in content_selectors:
                content_elem = soup.select_one(selector)
                if content_elem:
                    break
            
            # Fall back to body if no content container found
            content_elem = content_elem or soup.find("body") or soup
            
            # Remove unwanted elements
            for element in content_elem([
                "script", "style", "nav", "header", "footer", 
                "aside", "iframe", "form", "button", "input",
                "select", "textarea", "noscript"
            ]):
                element.decompose()
            
            # Clean up the text
            text_parts = []
            
            # Process headings and paragraphs
            for elem in content_elem.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li']):
                if elem.name.startswith('h'):
                    # Add extra newlines before headings for better separation
                    text_parts.append('\n\n' + elem.get_text(strip=True) + '\n')
                else:
                    text_parts.append(elem.get_text(strip=True))
            
            # Join all parts and clean up
            body_text = '\n'.join(text_parts)
            
            # Clean up whitespace and normalize newlines
            body_text = re.sub(r'\s+', ' ', body_text)  # Replace all whitespace with single space
            body_text = re.sub(r'\n{3,}', '\n\n', body_text)  # Limit consecutive newlines
            body_text = body_text.strip()
            
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
        output_folder: Optional[str] = None
    ) -> str:
        """
        Save an updated KB article.

        Args:
            article: The original KB article dictionary.
            updated_content: The updated content.
            output_folder: Directory to save the updated article. If None, saves in the same directory as the original.


        Returns:
            Path to the saved article.
        """
        article_id = article.get("id", os.path.splitext(os.path.basename(article["path"]))[0])
        
        # Determine the output directory
        if output_folder is None:
            # Default to the same directory as the original article
            output_dir = os.path.dirname(os.path.abspath(article["path"]))
        else:
            # Use the provided output directory
            output_dir = os.path.abspath(output_folder)
            
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create the output file path with _revised.html suffix
        output_file = os.path.join(output_dir, f"{article_id}_revised.html")
        
        try:
            with open(article["path"], "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
                
            # Find the main content element (this may need customization based on the HTML structure)
            content_elem = soup.find("div", class_="article-body") or soup.find("body")
            
            if content_elem:
                # Replace the content
                content_elem.clear()
                content_elem.append(BeautifulSoup(updated_content, "html.parser"))
                
                # Add CSS styles to highlight updated and removed content
                style_tag = soup.new_tag("style")
                style_tag.string = """
                .updated {
                    color: darkgreen;
                }
                .removed {
                    text-decoration: line-through;
                    color: darkred;
                }
                """
                
                # Add the style tag to the head, or create a head if it doesn't exist
                if soup.head:
                    soup.head.append(style_tag)
                else:
                    head = soup.new_tag("head")
                    head.append(style_tag)
                    if soup.html:
                        soup.html.insert(0, head)
                    else:
                        html = soup.new_tag("html")
                        html.append(head)
                        soup.append(html)
                
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