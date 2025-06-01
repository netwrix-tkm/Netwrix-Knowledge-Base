# KB Enhancement Prompting Flow

This document explains the flow of prompts in the KB article enhancement process.

## Overview

The system uses two separate phases with different prompts:
1. **Assessment Phase** - Determines if an article needs updates
2. **Update Phase** - Makes actual changes to the article content

## Prompt Flow Diagram

```
┌─────────────────────┐     ┌─────────────────────┐
│  ASSESSMENT PHASE   │     │     UPDATE PHASE    │
└─────────────┬───────┘     └────────────┬────────┘
              │                          │
┌─────────────▼───────┐     ┌────────────▼────────┐
│  Assessment System   │     │    Update System    │
│       Message        │     │       Message       │
└─────────────┬───────┘     └────────────┬────────┘
              │                          │
              │ "You are an expert      │ "You are a technical
              │  at assessing..."       │  documentation expert..."
              │                          │ + Style Guide + HTML Comment Instructions
┌─────────────▼───────┐     ┌────────────▼────────┐
│  Assessment User     │     │     Update User     │
│       Message        │     │       Message       │
└─────────────┬───────┘     └────────────┬────────┘
              │                          │
              │ - Article Content        │ - Article Content  
              │ - Reference Chunks       │ - Reference Chunks
              │ - JSON Format Request    │ 
              │                          │
┌─────────────▼───────┐     ┌────────────▼────────┐
│   GPT-4o-mini       │     │    GPT-4o-mini      │
│  (assessment model)  │     │    or GPT-4o        │
└─────────────┬───────┘     └────────────┬────────┘
              │                          │
┌─────────────▼───────┐     ┌────────────▼────────┐
│  JSON Response with  │     │  Updated Article    │
│  - update_level      │     │  with Change        │
│  - relevance_score   │     │  Explanations       │
│  - reasoning         │     │  (HTML format)      │
└───────────────────┬─┘     └──────────────────────┘
                    │
                    ▼
         ┌────────────────────┐
         │  Decision Logic    │
         │  (update_level)    │
         └──────────┬─────────┘
                    │
                    ▼
         ┌────────────────────┐
         │ "none"    → Skip   │
         │ "minor"   → Update │
         │ "major"   → Update │
         │          with GPT-4o│
         └────────────────────┘
```

## Detailed Prompts

### 1. Assessment Phase

#### Assessment System Message (Simple)
```
You are an expert at assessing knowledge base articles. 
Your task is to determine if an article needs updates based on provided reference information.

Respond in this exact JSON format:
{
  "relevant": true/false,
  "update_level": "none"/"minor"/"major",
  "relevance_score": 0.0-1.0,
  "reasoning": "brief explanation"
}

Where:
- "relevant": true if references contain information relevant to this article
...
```

#### Assessment User Message
```
Analyze the following article content and reference information.
Determine if the references are relevant to the article and if the article needs updates.

# ARTICLE CONTENT
[Article HTML content]

# REFERENCES
REFERENCE 1: [Reference text chunk 1]
REFERENCE 2: [Reference text chunk 2]
...
```

### 2. Update Phase

#### Update System Message (Comprehensive)
```
You are a technical documentation expert tasked with updating a knowledge base article 
using the most recent product documentation.

# INSTRUCTIONS
1. If the PROVIDED REFERENCES are relevant to the ARTICLE CONTENT, update the article content...
2. If the PROVIDED REFERENCES are not relevant to the ARTICLE CONTENT, do not make changes...
...
[10 more detailed instructions including formatting with spans and HTML comments]

# STYLE GUIDE
[Style guide content]
```

#### Update User Message (Simplified)
```
Your task is to update this Knowledge Base article using the provided reference documentation.

# ARTICLE TO UPDATE
[Article HTML content]

# REFERENCE DOCUMENTATION
REFERENCE 1: [Reference text chunk 1]
REFERENCE 2: [Reference text chunk 2]
...
```

### HTML Comments for Change Documentation

The system uses HTML comments to document changes, as specified in the system message:

```html
<!-- 
CHANGE EXPLANATION:
Documentation reference: "...exact quote from documentation..."
Relevance: Explain why this information was relevant to this section
Changes made: Describe what was changed and why
-->
```

This approach:
- Keeps the presentation layer clean (spans without reason attributes)
- Provides more detailed explanations in comments
- Makes it easier for reviewers to understand the rationale behind each change
- Separates styling from change documentation

## Model Selection Logic

```
if assessment result is "none":
    → No update needed
elif assessment result is "minor" OR force_update_level is not "major":
    → Use GPT-4o-mini for updates
else (assessment result is "major" OR force_update_level is "major"):
    → Use GPT-4o for more complex updates
```

This two-phase approach allows for efficient use of the models, using the smaller model when possible and the more powerful model only when necessary for complex updates. 