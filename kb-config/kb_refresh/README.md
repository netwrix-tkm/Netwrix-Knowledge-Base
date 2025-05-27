# KB Article Refresh Tool

A tool for refreshing knowledge base articles using PDF documentation.

## Features

- Extract and chunk PDF documentation with semantic section awareness
- Generate embeddings for document chunks using local sentence transformers
- Find relevant reference documentation chunks for KB articles using semantic search
- Refresh KB articles using Azure OpenAI, incorporating context from relevant documentation
- Flag outdated or inaccurate KB articles
- Generate reports on the refresh process

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set the following environment variables (or create a `.env` file):
   ```
   AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com
   AZURE_OPENAI_VERSION=2024-12-01-preview
   AZURE_OPENAI_API_KEY=your_api_key
   AZURE_OPENAI_MODEL=your_model_deployment_name
   ```

## Usage

### Quick Start

Run the tool on all products:

```bash
python kb-config/run.py
```

### Process a Single Product

```bash
python kb-config/run.py --product endpoint-protector
```

### Command Line Options

```bash
python kb-config/run.py --help
```

Options:
- `--pdf-dir`: Directory containing PDF files (default: "all-articles")
- `--html-dir`: Directory containing HTML KB articles (default: "all-articles-html")
- `--output-dir`: Directory to save refreshed articles (default: "refreshed-articles")
- `--embedding-dir`: Directory to save embeddings (default: "embeddings")
- `--embedder-model`: Name of the sentence-transformer model to use (default: "all-MiniLM-L6-v2")
- `--pdf-backend`: PDF extraction backend to use (choices: "pypdf2", "pdfplumber", default: "pypdf2")
- `--max-chunks`: Maximum number of document chunks to use per article (default: 5)
- `--similarity-threshold`: Minimum similarity score for retrieving chunks (default: 0.5)
- `--product`: Process a specific product (omit to process all)

## Project Structure

- `kb-config/`
  - `kb-refresh/`: Main package
    - `__init__.py`: Package initialization
    - `main.py`: Main orchestration module
    - `pdf_extractor.py`: PDF extraction module
    - `chunker.py`: Document chunking module
    - `embedder.py`: Text embedding module
    - `html_processor.py`: HTML processing module
    - `llm_client.py`: LLM client module for Azure OpenAI
    - `cli.py`: Command line interface
  - `run.py`: Simple wrapper script
  - `setup.py`: Setup script for installation 