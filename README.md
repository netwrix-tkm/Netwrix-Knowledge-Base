# CSV to Docusaurus MDX Converter

This tool converts the Netwrix Knowledge Base CSV file to Docusaurus-compatible MDX files.

## Features

- Extracts all fields as frontmatter
- Uses the Title field as the h1 heading
- Converts HTML in the Content__c column to markdown
- Creates MDX files with slugified filenames based on titles

## Usage

1. Install dependencies:
```bash
npm install
```

2. Run the converter:
```bash
npm run convert
```

The converted MDX files will be saved in the `./docs` directory.

## Customization

- To change the output directory, modify the `OUTPUT_DIR` constant in `convert_csv_to_mdx.js`
- You can adjust field handling in the script as needed 