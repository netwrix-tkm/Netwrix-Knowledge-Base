# KB Article Refresh Tool

This tool automatically refreshes knowledge base articles based on the latest PDF documentation.

## Quick Start

To refresh all articles for a specific product:

```bash
python run.py --product endpoint-protector
```

The `--product` parameter:
1. Locates the PDF documentation for that product
2. Processes the PDF to extract text and create embeddings
3. Finds all knowledge base articles related to that product
4. Updates each article with content from the PDF documentation

## Features

- Extract text from PDF documentation
- Chunk extracted text into semantic units
- Generate embeddings for efficient searching
- Compare KB articles to reference documentation
- Automatically refresh articles with the latest information
- Flag outdated content that requires manual review
- Generate reports on the refresh process

## Two-Model Approach

The tool uses a tiered approach with two model options:

1. **GPT-4o-mini-support**: A cost-effective model used for:
   - Initial assessment of whether an article needs updating
   - Processing articles that need only minor updates

2. **GPT-4o-support**: A more powerful model used for:
   - Processing articles that need major updates with complex content changes

This tiered approach optimizes for both cost and quality:
- Reduces costs by using the less expensive model when possible
- Maintains high quality by using the more powerful model for complex updates

## Usage

### Basic Usage

```bash
# Process all articles for a specific product
python run.py --product endpoint-protector

# Process a specific article with existing embeddings
python run.py --article-path path/to/article.html

# Process a directory of articles recursively
python run.py --article-path path/to/articles/ --recursive

# Process a PDF and specific article together
python run.py --pdf-path path/to/document.pdf --article-path path/to/article.html
```

### Model Selection

```bash
# Use GPT-4o-mini-support for both assessment and updates (most cost-effective)
python run.py --product endpoint-protector --assessment-model gpt-4o-mini-support --update-model gpt-4o-mini-support

# Use GPT-4o-support for both assessment and updates (highest quality, most expensive)
python run.py --product endpoint-protector --assessment-model gpt-4o-support --update-model gpt-4o-support

# Use tiered approach (default: mini for assessment, gpt-4o-support for major updates)
python run.py --product endpoint-protector --use-tiered
```

### Force Update Level

You can bypass the assessment phase and force a specific update level:

```bash
# Force treating all articles as needing minor updates (uses mini model)
python run.py --product endpoint-protector --force-update-level minor

# Force treating all articles as needing major updates (uses gpt-4o-support model)
python run.py --product endpoint-protector --force-update-level major
```

## Complete Command Line Options

### Basic Settings
- `--product`: Process a specific product (e.g., "endpoint-protector")
- `--article-path`: Path to a specific article or directory of articles
- `--article-ids`: Comma-separated list of specific article IDs to process (e.g., '12345,67890')
- `--max-articles`: Maximum number of articles to process per product (for testing)

### Directory Settings
- `--pdf-dir`: Directory containing PDF files (default: "doc-pdfs")
- `--html-dir`: Directory containing HTML KB articles (default: "all-articles-html")
- `--output-dir`: Directory to save refreshed articles (default: "refreshed-articles")
- `--embedding-dir`: Directory to save embeddings (default: "embeddings")

### PDF Processing
- `--pdf-path`: Path to a specific PDF file to process
- `--pdf-backend`: PDF extraction backend to use (choices: "pypdf2", "pdfplumber", default: "pypdf2")
- `--extract-only`: Just extract text from a PDF and save to a text file
- `--extract-and-chunk`: Extract text, chunk it, and save chunks to a JSON file
- `--extract-chunk-embed`: Extract text, chunk it, generate embeddings, and save to an embedding file

### Article Processing
- `--embeddings-path`: Direct path to a specific embeddings file (overrides automatic detection)
- `--recursive`: Process HTML files in subdirectories when using --article-path
- `--limit`: Limit processing to the first N articles in a directory

### Semantic Search Settings
- `--embedder-model`: Name of the sentence-transformer model to use (default: "all-MiniLM-L6-v2")
- `--max-chunks`: Maximum number of document chunks to use per article (default: 5)
- `--similarity-threshold`: Minimum similarity score for retrieving chunks (default: 0.3)

### LLM Model Settings
- `--assessment-model`: Model to use for article assessment (choices: "gpt-4o-mini-support", "gpt-4o-support", default: "gpt-4o-mini-support")
- `--update-model`: Model to use for article updates (choices: "gpt-4o-mini-support", "gpt-4o-support", default: "gpt-4o-support")
- `--force-update-level`: Force update level for all articles (choices: "none", "minor", "major")

## Common Workflows

### 1. Refresh All Articles for a Product

```bash
python run.py --product endpoint-protector
```

### 2. Process Multiple Articles in a Directory

```bash
python run.py --article-path all-articles-html/endpoint-protector/ --recursive
```

### 3. Test with a Limited Number of Articles

```bash
python run.py --product endpoint-protector --max-articles 5
```

### 4. Process a New PDF and Generate Embeddings

```bash
python run.py --pdf-path doc-pdfs/new-document.pdf --extract-chunk-embed
```

### 5. Process Specific Articles by ID

```bash
python run.py --article-ids "12345,67890" --embeddings-path embeddings/document_embeddings.jsonl
```

### 6. Extract Content from PDFs

```bash
# Just extract text from a PDF
python run.py --pdf-path doc-pdfs/document.pdf --extract-only

# Extract text and chunk it
python run.py --pdf-path doc-pdfs/document.pdf --extract-and-chunk

# Extract text, chunk it, and generate embeddings (full preprocessing)
python run.py --pdf-path doc-pdfs/document.pdf --extract-chunk-embed
```

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set the following environment variables (or create a `.env` file):
   ```
   AZURE_OPENAI_API_KEY=your_api_key
   AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com
   AZURE_OPENAI_VERSION=2024-12-01-preview
   ```

## Project Structure

- `kb-tools/`
  - `kb_enhance/`: Main enhancement package
    - `__init__.py`: Package initialization
    - `main.py`: Main orchestration module
    - `pdf_extractor.py`: PDF extraction module
    - `chunker.py`: Document chunking module
    - `embedder.py`: Text embedding module
    - `html_processor.py`: HTML processing module
    - `llm_client.py`: LLM client module for Azure OpenAI
    - `cli.py`: Command line interface
    - `run.py`: Simple wrapper script
  - `docs_references/`: Reference documents and extracted data
    - `extracted/`: Extracted PDF text
    - `chunked/`: Chunked documents
    - `embeddings/`: Document embeddings
  - `kb_evaluate/`: Evaluation package
    - `evaluate.py`: KB evaluation script
    - `assessor.py`: Article assessment tool
    - `reporter.py`: Reporting tool 