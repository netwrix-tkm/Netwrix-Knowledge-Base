"""
LLM Client Module

This module handles the integration with Azure OpenAI for article refreshing.
"""

import json
import os
import pathlib
from typing import Dict, List, Optional, Tuple, Union
from dotenv import load_dotenv

import requests


def load_style_guide() -> str:
    """
    Load the style guide content from the style_guide.md file.
    
    Returns:
        str: The content of the style guide.
    """
    try:
        # Get the directory where this script is located
        script_dir = pathlib.Path(__file__).parent.absolute()
        style_guide_path = script_dir / "style_guide.md"
        
        with open(style_guide_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Warning: Could not load style guide: {e}")
        return ""


class AzureOpenAIClient:
    """Client for the Azure OpenAI service."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        endpoint: Optional[str] = None,
        api_version: Optional[str] = None,
        model: Optional[str] = None
    ):
        """
        Initialize the Azure OpenAI client.

        Args:
            api_key: Azure OpenAI API key (defaults to env variable).
            endpoint: Azure OpenAI endpoint URL (defaults to env variable).
            api_version: API version (defaults to env variable).
            model: Model deployment name (defaults to env variable).
        """
        # Load environment variables
        load_dotenv()
        
        self.api_key = api_key or os.environ.get("AZURE_OPENAI_API_KEY")
        self.endpoint = endpoint or os.environ.get("AZURE_OPENAI_ENDPOINT")
        self.api_version = api_version or os.environ.get("AZURE_OPENAI_VERSION")
        self.model = model or os.environ.get("AZURE_OPENAI_MODEL")

        if not self.api_key or not self.endpoint or not self.api_version or not self.model:
            raise ValueError(
                "Azure OpenAI configuration is incomplete. "
                "Set AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, "
                "AZURE_OPENAI_VERSION, and AZURE_OPENAI_MODEL as environment variables."
            )

    def refresh_article(
        self, 
        article_content: str, 
        reference_chunks: List[Dict], 
        max_tokens: int = 4000,
        temperature: float = 0.0
    ) -> Tuple[str, bool]:
        """
        Refresh an article using Azure OpenAI.
        
        Args:
            article_content: The content of the article to refresh.
            reference_chunks: List of reference chunks to use for context.
            max_tokens: Maximum number of tokens to generate.
            temperature: Temperature parameter for generation.
            
        Returns:
            Tuple of (refreshed content, outdated flag).
        """
        # Load the style guide
        style_guide = load_style_guide()
        
        # Prepare the context from reference chunks
        context = ""
        for i, chunk in enumerate(reference_chunks):
            context += f"\nREFERENCE {i+1} (from {chunk.get('section_name', 'Unknown')}): {chunk.get('text', '')}\n"

        prompt = f"""
You are a technical documentation expert tasked with refreshing a knowledge base article using the most recent product documentation.

# INSTRUCTIONS
1. If the PROVIDED REFERENCES are relevant to the ARTICLE CONTENT, update the article content using the references.
2. If the PROVIDED REFERENCES are not relevant to the ARTICLE CONTENT, do not make any changes based on references. Simply mark the article as current.
3. Apply any changes needed to comply with the STYLE GUIDE regardless of reference relevance.
4. When references contradict the article, prioritize the reference information as it's more recent.
5. Output in HTML format. Do not use triple backticks or ```html.
6. Do not remove any images or links from the article.
7. Begin with a summary blockquote of your changes:

   <blockquote class="change-summary">
     <p><strong>Changes Made:</strong></p>
     <ul>
       <li>List each significant change</li>
       <li>Explain why each change was made</li>
     </ul>
   </blockquote>

8. For UPDATED content: 
   - Wrap with `<span class="updated" reason="why the content was updated based on the references">New content</span>`
   - Provide specific, detailed reasons referencing the source
   - Use for both additions and modifications

9. For that should be REMOVED:
   - Wrap with `<span class="removed" reason="why the content was removed based on the references">Original text</span>`
   - Leave the original text inside the span (do not delete it)
   - Explain specifically why it's outdated or incorrect

10. If the article is completely current and accurate, state this clearly in the summary blockquote.

# PROVIDED REFERENCES
{context}

# ARTICLE CONTENT
{article_content}

# STYLE GUIDE
{style_guide}

"""

        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key,
        }

        body = {
            "messages": [
                {"role": "system", "content": "You are a technical documentation expert."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }

        try:
            url = f"{self.endpoint}/openai/deployments/{self.model}/chat/completions?api-version={self.api_version}"
            response = requests.post(url, headers=headers, json=body)
            response.raise_for_status()
            
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            
            # Check if the content is flagged as outdated
            is_outdated = '<div class="outdated-warning">' in content
            
            return content, is_outdated
            
        except Exception as e:
            print(f"Error calling Azure OpenAI: {e}")
            return f"<p>Error refreshing article: {e}</p>", True 