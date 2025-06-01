# KB Enhancement Tasks for VS Code

This directory contains VS Code task configurations for enhancing KB articles using documentation PDFs. These tasks make it easy to run various KB enhancement operations directly from within VS Code.

## Available Tasks

To run any of these tasks:
1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
2. Type "Tasks: Run Task"
3. Select one of the KB enhancement tasks

### Current File/Folder Tasks

These tasks work on the currently open file or folder, making it even easier to process articles:

- **KB: Enhance Current Article**
  - Enhances the currently open HTML article using the latest documentation
  - No additional prompts required

### Enhancement Tasks

- **KB: Enhance Article**
  - Enhances a specific article using the latest documentation
  - Prompts for the article path

### PDF Processing Tasks

- **KB: Extract PDF**
  - Extracts raw text from a PDF and saves it to an extracted file
  - Prompts for PDF path

- **KB: Chunk Text File**
  - Processes an extracted text file into semantic chunks
  - Prompts for path to an extracted text file
  - Does NOT generate embeddings

- **KB: Embed Chunks**
  - Generates embeddings from a chunked JSON file 
  - Prompts for path to a chunked JSON file

## Local Storage

The KB enhancement tool stores all intermediate files locally in the `kb-tools/kb_enhance` directory:

- `extracted/` - Contains extracted text from PDFs
- `chunked/` - Contains JSON files with semantic chunks
- `embeddings/` - Contains JSONL files with vector embeddings

These directories are automatically created in the script folder, ensuring the tool works regardless of where the project is located.

## Task Input Values

When you run a task, VS Code will prompt you for input values:

- **pdfPath**: Path to PDF file (e.g., `product-name/new-document.pdf`)
- **articlePath**: Path to HTML article file (e.g., `all-articles-html/product-name/article.html`)

## Common Use Cases

### Enhancing a Currently Open Article

1. Open an HTML article file in VS Code
2. Run "KB: Enhance Current Article"
3. The article will be enhanced using the latest documentation

### Enhancing a Specific Article

1. Run "KB: Enhance Article"
2. Enter the path to the HTML article file
3. The article will be enhanced using the latest documentation

### Processing a PDF Document

To fully process a PDF document from extraction to embedding:

1. Run "KB: Embed Chunks" 
2. Enter the path to the PDF file
3. The script will extract text, chunk it, and generate embeddings

### Step-by-Step PDF Processing

For more control over the PDF processing pipeline:

1. Run "KB: Extract PDF" to extract the text
2. Run "KB: Chunk Extracted Text" to chunk the extracted text
3. Run "KB: Embed Chunks" to generate embeddings for the chunks 