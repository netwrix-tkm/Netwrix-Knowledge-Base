"""
Report Generator Module

Generates summary reports from article assessments.
"""

import os
import json
import datetime
import re
from typing import Dict, List, Any, Tuple
import requests
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

def estimate_tokens(text: str) -> int:
    """
    Estimate the number of tokens in a text string using a simple heuristic.
    
    Args:
        text: Input text
        
    Returns:
        Estimated token count
    """
    if not text:
        return 0
        
    # A very rough heuristic: 1 token is about 4 characters for English text
    # This is not perfect but gives a reasonable approximation
    return len(text) // 4

class ReportGenerator:
    """Generates summary reports from article assessments."""
    
    def __init__(
        self,
        output_dir: str = ".reports",
        api_key: str = None,
        endpoint: str = None,
        api_version: str = None,
        model: str = "gpt-4o-mini-support"
    ):
        """
        Initialize the report generator.
        
        Args:
            output_dir: Directory to save reports
            api_key: Azure OpenAI API key
            endpoint: Azure OpenAI endpoint
            api_version: API version
            model: Model to use for report generation
        """
        self.output_dir = output_dir
        # We'll determine the exact directory at report generation time
        
        # Load environment variables
        self.api_key = api_key or os.environ.get("AZURE_OPENAI_API_KEY")
        self.endpoint = endpoint or os.environ.get("AZURE_OPENAI_ENDPOINT")
        self.api_version = api_version or os.environ.get("AZURE_OPENAI_VERSION", "2024-12-01-preview")
        self.model = model
        
        # Define token costs per model ($ per token)
        self.token_costs = {
            "gpt-4o-mini": {
                "input": 0.15 / 1000000,  # $0.15 per 1M input tokens
                "output": 0.60 / 1000000,  # $0.60 per 1M output tokens
            },
            "gpt-4o": {
                "input": 5.00 / 1000000,   # $5.00 per 1M input tokens
                "output": 15.00 / 1000000,  # $15.00 per 1M output tokens
            }
        }

    def generate_report(self, product_name: str, assessments: List[Dict]) -> str:
        """
        Generate a summary report from article assessments.
        
        Args:
            product_name: Name of the product
            assessments: List of article assessments
            
        Returns:
            Path to the generated report
        """
        # First, find the product directory from the first article path
        product_dir = None
        if assessments and "article_path" in assessments[0]:
            article_path = assessments[0]["article_path"]
            # Get the directory containing the article
            product_dir = os.path.dirname(os.path.abspath(article_path))
        
        # If we can't determine the product directory, use a default
        if not product_dir:
            product_dir = os.path.join("all-articles-html", product_name)
            
        # Create the report directory in the product directory
        report_dir = os.path.join(product_dir, self.output_dir)
        os.makedirs(report_dir, exist_ok=True)
        
        # Save raw assessments JSON
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        raw_json_path = os.path.join(report_dir, f"raw_assessments_{timestamp}.json")
        with open(raw_json_path, 'w', encoding='utf-8') as f:
            json.dump(assessments, f, indent=2)
        
        # Sort assessments by priority
        priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "unknown": 4}
        sorted_assessments = sorted(
            assessments,
            key=lambda x: (
                priority_order.get(x.get("priority", "unknown"), 99),
                -x.get("score", 0)  # Higher scores first
            )
        )
        
        # Generate the report using LLM
        summarized_report = self._generate_summary_with_llm(product_name, sorted_assessments)
        
        # Save the report
        report_path = os.path.join(report_dir, f"kb_evaluation_report_{timestamp}.md")
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(summarized_report)
        
        return report_path

    def _format_assessments_for_llm(self, assessment_summaries):
        """
        Create a concise summary of assessments for the LLM with only essential fields.
        
        Args:
            assessment_summaries: Full list of assessment summaries
            
        Returns:
            Formatted string with concise assessment data
        """
        # Create simplified assessment list with only essential fields
        simplified_assessments = []
        
        for assessment in assessment_summaries:
            simplified_assessments.append({
                "title": assessment.get("title", "Untitled"),
                "score": assessment.get("score", 0),
                "recommendation": assessment.get("recommendation", "No recommendation"),
                "status": assessment.get("status", "unknown"),
                "priority": assessment.get("priority", "unknown"),
                "link_path": assessment.get("link_path", "#"),
                "summary": assessment.get("summary", "No detailed assessment available.")  # Include the original assessor's summary
            })
        
        # Calculate average score
        total_score = sum(assessment.get("score", 0) for assessment in assessment_summaries)
        avg_score = total_score / len(assessment_summaries) if assessment_summaries else 0
        
        # Count potential duplicates
        duplicate_count = sum(1 for a in assessment_summaries if a.get("has_duplicates", False))
        
        # Format the concise summary
        summary = f"""
# Assessment Summary
- Total Articles: {len(assessment_summaries)}
- Average Score: {avg_score:.1f}/100
- Articles with Potential Duplicates: {duplicate_count}

# Simplified Assessments (sorted by priority)
{json.dumps(simplified_assessments, indent=2) if simplified_assessments else "None"}
"""
        return summary

    def _generate_summary_with_llm(self, product_name: str, assessments: List[Dict]) -> str:
        """
        Generate a summary report using LLM.
        
        Args:
            product_name: Name of the product
            assessments: List of article assessments (sorted by priority)
            
        Returns:
            Generated report content
        """
        # If no assessments, return a simple report
        if not assessments:
            return f"# KB Evaluation Report: {product_name}\n\n*Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\nNo articles were assessed."
        
        # Prepare assessment summaries for LLM
        assessment_summaries = []
        for i, assessment in enumerate(assessments):
            # Extract just the filename from the path for better linking
            path = assessment.get("relative_path", assessment.get("article_path", ""))
            filename = os.path.basename(path)
            # Add ..\ prefix for proper linking in the report
            link_path = f"..\\{filename}"
            
            # Get key details for better reporting
            gaps = assessment.get("gaps", [])
            gaps_str = "; ".join(gaps) if gaps else "None identified"
            
            relevant_doc = ""
            if "relevant_chunks" in assessment and assessment["relevant_chunks"]:
                if isinstance(assessment["relevant_chunks"], list) and assessment["relevant_chunks"]:
                    chunk = assessment["relevant_chunks"][0]
                    relevant_doc = chunk.get("text", "")[:200] + "..." if len(chunk.get("text", "")) > 200 else chunk.get("text", "")
            
            # Process potential duplicates information
            potential_duplicates = []
            if "potential_duplicates" in assessment and assessment["potential_duplicates"]:
                for dup in assessment["potential_duplicates"]:
                    dup_filename = os.path.basename(dup.get("path", ""))
                    dup_path = f"..\\{dup_filename}"
                    potential_duplicates.append({
                        "title": dup.get("title", "Unknown"),
                        "path": dup_path,
                        "similarity_score": dup.get("similarity_score", 0.0)
                    })
            
            summary = {
                "index": i + 1,
                "title": assessment.get("title", "Untitled"),
                "status": assessment.get("status", "unknown"),
                "priority": assessment.get("priority", "unknown"),
                "score": assessment.get("score", 0),
                "summary": assessment.get("summary", "No summary provided"),
                "recommendation": assessment.get("recommendation", "No recommendation provided"),
                "gaps": gaps_str,
                "filename": filename,
                "link_path": link_path,
                "relevant_doc": relevant_doc,
                "potential_duplicates": potential_duplicates,
                "has_duplicates": len(potential_duplicates) > 0
            }
            assessment_summaries.append(summary)
        
        # Create summary statistics
        status_counts = {}
        priority_counts = {}
        total_score = 0
        duplicate_count = sum(1 for a in assessment_summaries if a["has_duplicates"])
        
        for assessment in assessments:
            status = assessment.get("status", "unknown")
            priority = assessment.get("priority", "unknown")
            score = assessment.get("score", 0)
            
            status_counts[status] = status_counts.get(status, 0) + 1
            priority_counts[priority] = priority_counts.get(priority, 0) + 1
            total_score += score
        
        # Calculate cost estimates using the token-based approach
        cost_details, total_cost = self.calculate_cost_estimate(assessments)
        
        minor_updates = cost_details["minor_updates"]
        major_updates = cost_details["major_updates"]
        
        avg_score = total_score / len(assessments) if assessments else 0
        
        # Prepare system message
        system_message = """You are an expert documentation analyst who specializes in creating concise and actionable summary reports.
Your task is to create a Markdown report that summarizes the state of a product's knowledge base articles.

Follow these guidelines:
1. Create a report with clear sections and headings
2. Organize information in tables by priority (critical first)
3. Include links to all files using the "link_path" value provided (do not use the filename directly)
4. Be concise but informative
5. Focus on actionable insights
6. Include statistics about the overall health of the KB
7. Highlight potential duplicate articles in a separate section when detected

IMPORTANT: Format the article list section as a Markdown table with the following columns:
1. Priority - The priority level (critical, high, medium, low)
2. Article - The article title with a link to the file (use the link_path value, e.g., [Article Title](..\\filename.html))
3. Score - The quality score of the article (0-100)
4. Recommendation - Use the "summary" field provided for each article, which contains the original assessment and recommendations from the article evaluator. This field already contains detailed feedback about what needs to be fixed.

Example table format:
```
| Priority | Article | Score | Recommendation |
|---------|---------|------|--------------|
| Critical | [Article Title](..\\filename.html) | 45 | The article contains outdated procedures and screenshots from version 3.2 while the current version is 4.0. The authentication section needs to be completely rewritten to reflect the new OAuth implementation. |
```

Include a separate section for potential duplicates if any are found, with a table showing the potentially duplicate articles.

Include a "Strategy Recommendations" section that provides practical advice on how to efficiently address the identified issues using AI tools. Consider:
1. Prioritization strategy (e.g., focus on critical articles first, address outdated sections of high-traffic articles)
2. AI-assisted workflow recommendations (e.g., using KB Enhancement tools for different types of updates)
3. Efficiency tips for faster updates (e.g., batching similar issues, updating templates)
4. Resource allocation guidance (how to best utilize the limited Technical Knowledge Manager resources)
5. Time-saving approaches specific to the issues found

Be specific and practical in your recommendations, tailored to the exact issues found in this assessment. Remember there is only ONE Technical Knowledge Manager available to address all issues.

AT THE END OF THE REPORT, add a "Cost Estimation" section that shows the token-based cost calculation with these details:
- Articles needing minor updates (GPT-4o-mini): Show average token count and cost per article
- Articles needing major updates (GPT-4o): Show average token count and cost per article

Note: Major updates include both "outdated" and "critical" status articles, as they're both updated using GPT-4o.

Calculate the total estimated cost to update all articles needing updates and show per-category costs.
Format this as a detailed table showing article counts, token counts, and costs.
"""

        # Initialize report cost to a default value in case the calculation fails
        report_cost = {
            "input_tokens": 0,
            "output_tokens": 0,
            "input_cost": 0,
            "output_cost": 0,
            "total_cost": 0
        }
        
        # Prepare user message
        user_message = f"""
Please create a KB health assessment report for {product_name} based on the following assessment data.

{self._format_assessments_for_llm(assessment_summaries)}

# Cost Estimation Data
- Articles needing minor updates: {minor_updates['count']} articles, avg cost: ${minor_updates['cost_per_article']:.4f} each
- Articles needing major updates: {major_updates['count']} articles, avg cost: ${major_updates['cost_per_article']:.4f} each
- Total estimated cost: ${total_cost:.2f}

Create a report with the following sections:
1. Executive Summary 
2. Overall Health Assessment
3. Recommendations by Priority
4. Strategy Recommendations

In the Strategy Recommendations section, provide practical advice on how a single Technical Knowledge Manager can efficiently address the identified issues using AI tools. Consider prioritization strategies, AI-assisted workflows, efficiency tips, and resource allocation guidance.

Format the article list as a table with these columns:
- Priority (critical, high, medium, low)
- Article (title with link using the link_path property)
- Score (0-100) 
- Recommendation (use the "summary" field provided for each article)

Sort the table by priority (critical first, then high, medium, low).

Use the original assessor's summary for each article in the Recommendation column - this summary already contains detailed feedback about what needs to be fixed.

If there are potential duplicates, include a separate section with a table showing duplicate articles.
"""

        # Calculate the cost of running this report
        report_cost = self.calculate_report_cost(system_message, user_message)
        
        # Add report cost to overall cost
        total_cost += report_cost["total_cost"]
        
        # Update the system message to include report cost
        system_message += f"""
Also include the cost of generating this report itself, which uses GPT-4o-mini:
- Input tokens: {report_cost["input_tokens"]}
- Output tokens: {report_cost["output_tokens"]} (estimated)
- Total report generation cost: ${report_cost["total_cost"]:.4f}
"""
        
        # Update the user message to include report cost
        user_message += f"""
# Report Generation Cost
- Input tokens: {report_cost["input_tokens"]}
- Output tokens: {report_cost["output_tokens"]} (estimated)
- Report generation cost: ${report_cost["total_cost"]:.4f}

Please include the report generation cost in the Cost Estimation section.
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
            "max_tokens": 4000,
            "temperature": 0.0
        }

        try:
            url = f"{self.endpoint}/openai/deployments/{self.model}/chat/completions?api-version={self.api_version}"
            response = requests.post(url, headers=headers, json=body)
            response.raise_for_status()
            
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            
            # Add a header with timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            header = f"""*Generated on: {timestamp}*

"""
            
            return header + content
            
        except Exception as e:
            print(f"Error generating summary report: {e}")
            # Return a basic report with a table
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            report = f"""*Generated on: {timestamp}*

# KB Evaluation Report: {product_name}

## Raw Assessment Summary

Total Articles: {len(assessments)}

### Articles by Priority

| Priority | Article | Score | Recommendation |
|---------|---------|------|--------------|
"""
            # Add basic article list
            for priority in ["critical", "high", "medium", "low", "unknown"]:
                articles = [a for a in assessments if a.get("priority") == priority]
                for article in articles:
                    title = article.get("title", "Untitled")
                    path = article.get("article_path", "#")
                    filename = os.path.basename(path)
                    link_path = f"..\\{filename}"
                    score = article.get("score", 0)
                    recommendation = article.get("summary", article.get("recommendation", "No recommendation"))
                    
                    report += f"| {priority.upper()} | [{title}]({link_path}) | {score} | {recommendation} |\n"
            
            # Check if there are any potential duplicates and add a section for them
            has_duplicates = any("potential_duplicates" in a and a["potential_duplicates"] for a in assessments)
            if has_duplicates:
                report += f"\n\n### Potential Duplicate Articles\n\n"
                report += "| Article | Potential Duplicate | Similarity |\n"
                report += "|---------|------------------|-------------|\n"
                
                for article in assessments:
                    title = article.get("title", "Untitled")
                    path = article.get("article_path", "#")
                    filename = os.path.basename(path)
                    link_path = f"..\\{filename}"
                    
                    if "potential_duplicates" in article and article["potential_duplicates"]:
                        for dup in article["potential_duplicates"]:
                            dup_title = dup.get("title", "Unknown")
                            dup_path = dup.get("path", "#")
                            dup_filename = os.path.basename(dup_path)
                            dup_link_path = f"..\\{dup_filename}"
                            similarity = dup.get("similarity_score", 0.0) * 100
                            
                            report += f"| [{title}]({link_path}) | [{dup_title}]({dup_link_path}) | {similarity:.1f}% |\n"
            
            # Add cost estimation at the end of the report
            report += f"""
## Error Generating Report

There was an error generating the detailed report: {e}

## Strategy Recommendations

When addressing the issues in this knowledge base with limited resources (one Technical Knowledge Manager):

1. **Prioritize Critical Items First**: Focus on articles marked as critical, especially those with the lowest scores.
2. **Use AI-Assisted Updates**: Leverage the KB Enhancement tools with the following workflow:
   - For critical articles: Use full GPT-4o model for comprehensive rewrites
   - For high-priority articles with scores below 50: Use AI-assisted updates with manual review
   - For medium/low priority articles: Consider batch processing with lighter AI assistance
3. **Batch Similar Issues**: Group articles with similar problems and update them together
4. **Create Templates**: For recurring issue types, develop templates that can be quickly adapted

## Cost Estimation

| Update Type | Count | Avg Tokens | Cost per Article | Total |
|-------------|-------|------------|-----------------|-------|
| Minor Updates (GPT-4o-mini) | {minor_updates['count']} | {minor_updates['avg_tokens']} | ${minor_updates['cost_per_article']:.4f} | ${minor_updates['total_cost']:.2f} |
| Major Updates (GPT-4o) | {major_updates['count']} | {major_updates['avg_tokens']} | ${major_updates['cost_per_article']:.4f} | ${major_updates['total_cost']:.2f} |
| Report Generation (GPT-4o-mini) | 1 | {report_cost["input_tokens"]} | ${report_cost["total_cost"]:.4f} | ${report_cost["total_cost"]:.2f} |
| **Total** | **{minor_updates['count'] + major_updates['count'] + 1}** | | | **${total_cost:.2f}** |
"""
            
            return report 

    def calculate_cost_estimate(self, assessments: List[Dict]) -> Tuple[Dict, float]:
        """
        Calculate a more accurate cost estimate based on token counts.
        
        Args:
            assessments: List of article assessments
            
        Returns:
            Tuple of (cost_details, total_cost)
        """
        # Group articles by status
        status_articles = {
            "needs_update": [],
            "outdated": [],
            "critical": [],
            "current": []
        }
        
        for assessment in assessments:
            status = assessment.get("status", "unknown")
            if status in status_articles:
                status_articles[status].append(assessment)
        
        # Define the assessment system prompt
        assessment_system_prompt = """You are an expert technical documentation evaluator who specializes in assessing knowledge base articles.
Your task is to evaluate a knowledge base article based on its content and the provided reference documentation."""
        
        # Calculate costs for each category
        minor_updates = status_articles["needs_update"]
        major_updates = status_articles["outdated"] + status_articles["critical"]  # Combine outdated and critical
        
        # Calculate average token counts for each category
        avg_minor_tokens = 0
        avg_major_tokens = 0
        
        # Count the actual content length in each category
        def estimate_article_tokens(article):
            """Estimate tokens from an article assessment object"""
            tokens = estimate_tokens(assessment_system_prompt)
            tokens += estimate_tokens(article.get("title", ""))
            
            # The content isn't stored in the assessment, but summary is available
            # and can give us a rough estimate of content length
            tokens += estimate_tokens(article.get("summary", "")) * 5  # Rough multiplier
            
            # Add tokens for relevant chunks
            for chunk in article.get("relevant_chunks", []):
                tokens += estimate_tokens(chunk.get("text", ""))
            
            return tokens
        
        # Sample for minor updates
        if minor_updates:
            sample_count = min(5, len(minor_updates))
            sample_tokens = sum(estimate_article_tokens(minor_updates[i]) for i in range(sample_count))
            avg_minor_tokens = sample_tokens // sample_count if sample_count > 0 else 0
        
        # Sample for major updates
        if major_updates:
            sample_count = min(5, len(major_updates))
            sample_tokens = sum(estimate_article_tokens(major_updates[i]) for i in range(sample_count))
            avg_major_tokens = sample_tokens // sample_count if sample_count > 0 else 0
        
        # If we don't have sufficient data, use reasonable defaults
        if avg_minor_tokens == 0:
            avg_minor_tokens = 2000  # Reasonable default
        if avg_major_tokens == 0:
            avg_major_tokens = 3500  # Reasonable default
        
        # Calculate costs using token-based pricing
        # Minor updates use GPT-4o-mini
        minor_update_cost = (
            self.token_costs["gpt-4o-mini"]["input"] * avg_minor_tokens +
            self.token_costs["gpt-4o-mini"]["output"] * 600  # Assume 600 output tokens
        )
        
        # Major updates use GPT-4o
        major_update_cost = (
            self.token_costs["gpt-4o"]["input"] * avg_major_tokens +
            self.token_costs["gpt-4o"]["output"] * 1000  # Assume 1000 output tokens
        )
        
        # Calculate total cost
        total_minor_cost = len(minor_updates) * minor_update_cost
        total_major_cost = len(major_updates) * major_update_cost
        total_cost = total_minor_cost + total_major_cost
        
        # Return cost details
        cost_details = {
            "minor_updates": {
                "count": len(minor_updates),
                "avg_tokens": avg_minor_tokens,
                "cost_per_article": minor_update_cost,
                "total_cost": total_minor_cost
            },
            "major_updates": {
                "count": len(major_updates),
                "avg_tokens": avg_major_tokens,
                "cost_per_article": major_update_cost,
                "total_cost": total_major_cost
            }
        }
        
        return cost_details, total_cost 

    def calculate_report_cost(self, system_message: str, user_message: str) -> Dict[str, Any]:
        """
        Calculate the cost of generating the report itself.
        
        Args:
            system_message: System prompt used for report generation
            user_message: User message used for report generation
            
        Returns:
            Report cost details including input tokens, output tokens, and total cost
        """
        # Estimate input tokens
        input_tokens = estimate_tokens(system_message) + estimate_tokens(user_message)
        
        # Estimate output tokens (a generous estimate for a detailed markdown report)
        output_tokens = 3000
        
        # Calculate cost using GPT-4o-mini pricing
        input_cost = self.token_costs["gpt-4o-mini"]["input"] * input_tokens
        output_cost = self.token_costs["gpt-4o-mini"]["output"] * output_tokens
        total_cost = input_cost + output_cost
        
        return {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "input_cost": input_cost,
            "output_cost": output_cost,
            "total_cost": total_cost
        } 