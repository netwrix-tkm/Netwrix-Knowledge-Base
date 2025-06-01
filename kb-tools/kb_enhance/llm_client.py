"""
LLM Client Module

This module handles the integration with Azure OpenAI for article refreshing.
"""

import json
import os
import pathlib
from typing import Dict, List, Optional, Tuple, Union
from dotenv import load_dotenv
import time

import requests


def load_style_guide() -> str:
    """
    Load the style guide content from the style guide files.
    Looks for files in the following locations (in order):
    1. kb-tools/style_guide/style_guide_mini.md
    2. kb-tools/style_guide/style_guide.md
    3. kb-tools/kb_enhance/style_guide_mini.md (legacy location)
    4. kb-tools/kb_enhance/style_guide.md (legacy location)
    
    Returns:
        str: The content of the style guide.
    """
    try:
        # Get the directory where this script is located
        script_dir = pathlib.Path(__file__).parent.absolute()
        
        # Check the new path first (in kb-tools/style_guide)
        style_guide_dir = script_dir.parent / "style_guide"
        
        # Try to load the mini style guide first from the new location
        mini_style_guide_path = style_guide_dir / "style_guide_mini.md"
        if mini_style_guide_path.exists():
            with open(mini_style_guide_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"Loaded mini style guide ({len(content)} characters)")
                return content
                
        # Fall back to the full style guide from the new location
        style_guide_path = style_guide_dir / "style_guide.md"
        if style_guide_path.exists():
            with open(style_guide_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"Loaded full style guide ({len(content)} characters)")
                return content
                
        # If not found in the new location, try the old locations
        mini_style_guide_path = script_dir / "style_guide_mini.md"
        if mini_style_guide_path.exists():
            with open(mini_style_guide_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"Loaded mini style guide from old location ({len(content)} characters)")
                return content
                
        # Fall back to the full style guide in the old location
        style_guide_path = script_dir / "style_guide.md"
        if style_guide_path.exists():
            with open(style_guide_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"Loaded full style guide from old location ({len(content)} characters) - consider moving to new location")
                return content
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
        assessment_model: str = "gpt-4o-mini-support",
        update_model: str = "gpt-4o-support"
    ):
        """
        Initialize the Azure OpenAI client.

        Args:
            api_key: Azure OpenAI API key (defaults to env variable).
            endpoint: Azure OpenAI endpoint URL (defaults to env variable).
            api_version: API version (defaults to env variable).
            assessment_model: Model for initial assessment (default: gpt-4o-mini-support).
            update_model: Model for content updates (default: gpt-4o-support).
        """
        # Load environment variables
        load_dotenv()
        
        self.api_key = api_key or os.environ.get("AZURE_OPENAI_API_KEY")
        self.endpoint = endpoint or os.environ.get("AZURE_OPENAI_ENDPOINT")
        self.api_version = api_version or os.environ.get("AZURE_OPENAI_VERSION")
        
        # Store both models
        self.assessment_model = assessment_model
        self.update_model = update_model

        if not self.api_key or not self.endpoint or not self.api_version:
            raise ValueError(
                "Azure OpenAI configuration is incomplete. "
                "Set AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, "
                "and AZURE_OPENAI_VERSION as environment variables."
            )
        
        # Cache the style guide when the client is initialized
        self.style_guide = load_style_guide()
        print(f"Style guide loaded and cached ({len(self.style_guide)} characters)")
        
        # Create a persistent system message with instructions and style guide
        self.system_message = self._create_system_message(self.style_guide)
        print("System message created with instructions and style guide")
        
        # Create assessment system message
        self.assessment_system_message = """You are an expert at assessing knowledge base articles. 
Your task is to determine if an article needs updates based on provided reference information.

Respond in this exact JSON format:
{{
  "relevant": true/false,
  "update_level": "none"/"minor"/"major",
  "relevance_score": 0.0-1.0,
  "reasoning": "brief explanation"
}}

Where:
- "relevant": true if references contain information relevant to this article
- "update_level": 
  - "none": no updates needed (article is current)
  - "minor": small factual corrections needed (style, typos, name changes, etc.)
  - "major": significant content updates needed (outdated procedures, missing information, etc.)
- "relevance_score": number from 0.0 (not relevant) to 1.0 (highly relevant)
- "reasoning": brief explanation of your assessment"""


    def assess_article_relevance(
        self,
        article_content: str,
        reference_chunks: List[Dict],
        max_tokens: int = 500,
        temperature: float = 0.0
    ) -> Tuple[str, float, str]:
        """
        Assess if references are relevant to the article and determine the update complexity.
        
        Args:
            article_content: The content of the article to assess
            reference_chunks: List of reference chunks to analyze
            max_tokens: Maximum number of tokens to generate
            temperature: Temperature parameter for generation
            
        Returns:
            Tuple of (update_level, relevance_score, reasoning)
            update_level can be "none", "minor", or "major"
            relevance_score is 0-1 indicating reference relevance
            reasoning is a string explaining the assessment
        """
        # Prepare the context from reference chunks
        context = ""
        for i, chunk in enumerate(reference_chunks):
            context += f"\nREFERENCE {i+1}: {chunk.get('text', '')}\n"
        
        user_message = f"""
Analyze the following article content and reference information.
Determine if the references are relevant to the article and if the article needs updates.

# ARTICLE CONTENT
{article_content}

# REFERENCES
{context}"""

        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key,
        }

        body = {
            "messages": [
                {"role": "system", "content": self.assessment_system_message},
                {"role": "user", "content": user_message}
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
            "response_format": {"type": "json_object"}
        }

        try:
            # Use the assessment model (gpt-4o-mini)
            url = f"{self.endpoint}/openai/deployments/{self.assessment_model}/chat/completions?api-version={self.api_version}"
            response = requests.post(url, headers=headers, json=body)
            response.raise_for_status()
            
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            
            # Parse the JSON response
            assessment = json.loads(content)
            update_level = assessment.get("update_level", "none")
            relevance_score = assessment.get("relevance_score", 0.0)
            reasoning = assessment.get("reasoning", "")
            
            print(f"Assessment: {update_level} updates needed (relevance: {relevance_score:.2f})")
            print(f"Reasoning: {reasoning}")
            
            return update_level, relevance_score, reasoning
            
        except Exception as e:
            print(f"Error calling assessment model: {e}")
            # Default to major update if there's an error
            return "major", 0.5, f"Error in assessment: {str(e)}"

    def refresh_article(
        self, 
        article_content: str, 
        reference_chunks: List[Dict], 
        max_tokens: int = 4000,
        temperature: float = 0.0,
        force_update_level: Optional[str] = None,
        assessment_result: Optional[Dict] = None
    ) -> Tuple[str, bool]:
        """
        Refresh an article based on reference chunks.
        
        Args:
            article_content: Content of the article to refresh.
            reference_chunks: Reference chunks to use for refreshing.
            max_tokens: Maximum tokens to generate.
            temperature: Temperature for generation.
            force_update_level: Force a specific update level.
            assessment_result: Assessment results from article relevance check.
            
        Returns:
            Tuple of (refreshed content, outdated flag).
        """
        # Format reference chunks into context
        context = ""
        for i, chunk in enumerate(reference_chunks):
            context += f"\nREFERENCE {i+1}: {chunk.get('text', '')}\n"
            
        # Determine which model to use based on complexity
        # Default to assessment model for minor updates, update model for major ones
        model = self.assessment_model  # Default to the simpler model
        
        # If forced, use the corresponding model
        if force_update_level == "major":
            print("Using update model due to forced major update level")
            model = self.update_model

        # Add assessment information to the user message if available
        assessment_info = ""
        if assessment_result:
            relevance_score = assessment_result.get("relevance_score", 0.0)
            reasoning = assessment_result.get("reasoning", "No reasoning provided")
            update_level = assessment_result.get("update_level", "unknown")
            
            assessment_info = f"""
# ASSESSMENT INFORMATION
- Relevance Score: {relevance_score:.2f} (0-1 scale)
- Update Level: {update_level}
- Assessment Reasoning: {reasoning}

"""
        
        user_message = f"""
Your task is to update this Knowledge Base article using the provided reference documentation.
{assessment_info}

# ARTICLE TO UPDATE
{article_content}

# REFERENCE DOCUMENTATION
{context}
"""

        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key,
        }

        body = {
            "messages": [
                # Use the persistent system message with instructions and style guide
                {"role": "system", "content": self.system_message},
                # Send only the references and article content in the user message
                {"role": "user", "content": user_message}
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }

        try:
            # Choose model based on update level
            model = self.update_model if force_update_level == "major" else self.assessment_model
            
            # More concise message about model selection
            if not os.environ.get("QUIET"):
                if force_update_level:
                    print(f"Using model: {model}")
            
            url = f"{self.endpoint}/openai/deployments/{model}/chat/completions?api-version={self.api_version}"
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

    def _create_system_message(self, style_guide: str) -> str:
        """
        Create the system message containing instructions and style guide.
        
        Args:
            style_guide: The style guide content
            
        Returns:
            The formatted system message
        """
        return f"""You are a technical documentation expert tasked with updating a knowledge base article using the most recent product documentation.

# INSTRUCTIONS
1. If provided, use the ASSESSMENT INFORMATION to guide your updates. It contains:
   - Relevance Score: The level of relevance of the references to the article (0=not relevant, 1=highly relevant)
   - Update Level: The recommended update level (none, minor, or major)
   - Assessment Reasoning: Explanation of what needs updating and why

2. If the PROVIDED REFERENCES are relevant to the ARTICLE CONTENT, update the article content using the references.
3. If the PROVIDED REFERENCES are not relevant to the ARTICLE CONTENT, do not make any changes based on references. Simply mark the article as current.
4. Apply any changes needed to comply with the STYLE GUIDE regardless of reference relevance.
5. When references contradict the article, prioritize the reference information as it's more recent.
6. Output in HTML format, but do not use triple backticks (```html).
7. Do not remove any images or links from the article.
8. Begin with a summary of your changes as an HTML comment:

   <!-- 
   CHANGE SUMMARY:
   - List each significant change
   - Explain why each change was made
   - If the article is completely current and accurate, state this clearly
   -->

9. Mark content changes in the output HTML using EXACTLY these three distinct styling approaches:

   A. UPDATED content (modified from original):
      - Wrap with `<span class="updated">Modified content</span>`
      - After each updated span, add an HTML comment explaining the change:
      
      <!-- 
      CHANGE EXPLANATION:
      Documentation reference: "...exact quote from documentation..."
      Updated: A summary of what was updated and why the content was updated
      -->

   B. NEW content (completely new sections/information):
      - Wrap with `<span class="new-content">Brand new content</span>`
      - After each new content span, add an HTML comment explaining the addition:
      
      <!-- 
      ADDITION EXPLANATION:
      Documentation reference: "...exact quote from documentation..."
      Added: A summary of what was added and why this content was added
      -->

   C. Content that should be REMOVED:
      - Wrap with `<span class="removed">Original text to remove</span>`
      - After each removed span, add an HTML comment explaining the removal:
      
      <!-- 
      REMOVAL EXPLANATION:
      Documentation reference: "...exact quote from documentation..."
      Removed: A summary of what was removed and why it needed to be removed
      -->

10. IMPORTANT: Format notes, cautions, and important notices using blockquote tags AND properly combine with change tracking. Always follow these EXACT HTML structures:

    A. For a NOTE that is being updated:
    ```
    <span class="updated">
      <blockquote>
        <p><span class="Note"><strong>NOTE: </strong></span>Updated note content here.</p>
      </blockquote>
    </span>
    <!-- 
    CHANGE EXPLANATION:
    Documentation reference: "...exact quote from documentation..."
    Updated: A summary of what was updated and why the content was updated
    -->
    ```

    B. For an IMPORTANT notice that is new content:
    ```
    <span class="new-content">
      <blockquote>
        <p><span class="Caution"><strong>IMPORTANT: </strong></span>New important warning here.</p>
      </blockquote>
    </span>
    <!-- 
    ADDITION EXPLANATION:
    Documentation reference: "...exact quote from documentation..."
    Added: A summary of what was added and why this content was added
    -->
    ```

    C. For a WARNING that is being removed:
    ```
    <span class="removed">
      <blockquote>
        <p><span class="Warning"><strong>WARNING: </strong></span>Outdated warning content.</p>
      </blockquote>
    </span>
    <!-- 
    REMOVAL EXPLANATION:
    Documentation reference: "...exact quote from documentation..."
    Removed: A summary of what was removed and why it needed to be removed
    -->
    ```
      
    These specific HTML structures MUST be followed exactly to maintain both proper styling and change tracking.

# STYLE GUIDE
{style_guide}""" 