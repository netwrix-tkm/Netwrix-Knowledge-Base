"""
LLM Client Module

This module handles the integration with Azure OpenAI for article refreshing.
"""

import json
import os
from typing import Dict, List, Optional, Tuple, Union
from dotenv import load_dotenv

import requests


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
        temperature: float = 0.3
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
        # Prepare the context from reference chunks
        context = ""
        for i, chunk in enumerate(reference_chunks):
            context += f"\nREFERENCE {i+1} (from {chunk.get('section_name', 'Unknown')}): {chunk.get('text', '')}\n"

        prompt = f"""
You are a technical documentation expert tasked with refreshing a knowledge base article using the most recent product documentation.

Instructions:
1. Use the PROVIDED REFERENCE material to update the ARTICLE CONTENT with accurate, current information.
2. Maintain the original structure, style and tone of the article.
3. Integrate useful facts, descriptions, and procedures from the references into the article.
4. If the article content contradicts the references, prioritize the reference information as it is more recent.
5. Output HTML format for the refreshed content.

REFERENCES:
{context}

ARTICLE CONTENT:
{article_content}

OUTPUT:
Provide your updated version of the article in valid HTML format.
If you detect that the article is substantially outdated or contains significant inaccuracies compared to the references, add "<div class="outdated-warning">This article contains outdated information and requires review.</div>" at the beginning.
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