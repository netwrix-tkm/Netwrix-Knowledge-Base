"""
Article Assessor Module

Evaluates KB articles against documentation using LLM.
"""

import os
import json
import datetime
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

class ArticleAssessor:
    """Assesses KB articles against documentation using LLM."""
    
    def __init__(
        self, 
        api_key: Optional[str] = None,
        endpoint: Optional[str] = None,
        api_version: Optional[str] = None,
        model: str = "gpt-4o-mini-support"
    ):
        """
        Initialize the assessor.
        
        Args:
            api_key: Azure OpenAI API key
            endpoint: Azure OpenAI endpoint
            api_version: API version
            model: Model to use for assessment
        """
        # Load environment variables
        self.api_key = api_key or os.environ.get("AZURE_OPENAI_API_KEY")
        self.endpoint = endpoint or os.environ.get("AZURE_OPENAI_ENDPOINT")
        self.api_version = api_version or os.environ.get("AZURE_OPENAI_VERSION")
        self.model = model
        
        if not self.api_key or not self.endpoint or not self.api_version:
            raise ValueError(
                "Azure OpenAI configuration is incomplete. "
                "Set AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, "
                "and AZURE_OPENAI_VERSION as environment variables."
            )

    def assess_article(
        self,
        article_path: str,
        article_content: str,
        article_title: str,
        created_date: Optional[str],
        modified_date: Optional[str],
        relevant_chunks: List[Dict]
    ) -> Dict[str, Any]:
        """
        Assess an article against documentation.
        
        Args:
            article_path: Path to the article
            article_content: Content of the article
            article_title: Title of the article
            created_date: Date the article was created
            modified_date: Date the article was last modified
            relevant_chunks: List of relevant documentation chunks
            
        Returns:
            Assessment dictionary
        """
        # Format reference chunks into context
        context = ""
        for i, chunk in enumerate(relevant_chunks):
            context += f"\nREFERENCE {i+1}: {chunk.get('text', '')}\n"
            if 'similarity_score' in chunk:
                context += f"Relevance score: {chunk['similarity_score']:.2f}/1.0\n"
        
        # Format dates
        date_info = ""
        if created_date:
            date_info += f"Created date: {created_date}\n"
        if modified_date:
            date_info += f"Last modified date: {modified_date}\n"
        
        system_message = """You are an expert technical documentation evaluator who specializes in assessing knowledge base articles.
Your task is to evaluate a knowledge base article based on its content and the provided reference documentation.

Respond with a JSON object with the following structure:

{
  "status": "current" | "needs_update" | "outdated" | "critical",
  "priority": "low" | "medium" | "high" | "critical",
  "score": 0-100,
  "age_assessment": "String evaluating article age vs content",
  "accuracy_assessment": "String evaluating accuracy compared to reference docs",
  "completeness_assessment": "String evaluating completeness",
  "technical_assessment": "String evaluating technical accuracy",
  "gaps": ["List of identified gaps or missing information"],
  "recommendation": "Short action recommendation (add/update/rewrite/no action)",
  "summary": "Brief summary of overall assessment"
}

Where:
- status: Overall assessment of the article
  - "current": Up-to-date with correct information
  - "needs_update": Minor updates required
  - "outdated": Significant updates required
  - "critical": Severely out-of-date, incorrect, or harmful content
- priority: How urgently the article needs attention
- score: 0-100 quality score (consider accuracy, completeness, freshness)
- Provide specific, actionable feedback in the assessment fields
"""
        
        user_message = f"""
# ARTICLE TO ASSESS
Title: {article_title}
{date_info}

Content:
{article_content}

# REFERENCE DOCUMENTATION
{context}

Based on the article content and reference documentation, please provide a comprehensive assessment.
"""

        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key,
        }

        body = {
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            "max_tokens": 800,
            "temperature": 0.1,
            "response_format": {"type": "json_object"}
        }

        try:
            url = f"{self.endpoint}/openai/deployments/{self.model}/chat/completions?api-version={self.api_version}"
            response = requests.post(url, headers=headers, json=body)
            response.raise_for_status()
            
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            
            # Parse the JSON response
            assessment = json.loads(content)
            
            # Add metadata
            assessment["article_path"] = article_path
            assessment["title"] = article_title
            assessment["assessed_at"] = datetime.datetime.now().isoformat()
            assessment["relative_path"] = os.path.relpath(article_path)
            assessment["relevant_chunks"] = relevant_chunks
            
            return assessment
            
        except Exception as e:
            print(f"Error assessing article {article_path}: {e}")
            return {
                "article_path": article_path,
                "title": article_title,
                "status": "error",
                "error_message": str(e),
                "priority": "unknown",
                "assessed_at": datetime.datetime.now().isoformat(),
                "relative_path": os.path.relpath(article_path),
                "relevant_chunks": relevant_chunks
            } 