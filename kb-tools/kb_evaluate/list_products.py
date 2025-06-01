#!/usr/bin/env python3
"""
List all product folders in the all-articles-html directory.
Output in format suitable for VS Code tasks.json.
"""

import os
import json
import sys

def main():
    """List all product folders and print them in JSON format."""
    try:
        # Find the project root directory (where README.md is located)
        project_root = find_project_root()
        
        # Path to the all-articles-html directory
        articles_dir = os.path.join(project_root, "all-articles-html")
        
        # Get all directories in all-articles-html
        product_folders = []
        if os.path.exists(articles_dir) and os.path.isdir(articles_dir):
            product_folders = [d for d in os.listdir(articles_dir) 
                              if os.path.isdir(os.path.join(articles_dir, d)) and not d.startswith('.')]
            product_folders.sort()  # Sort alphabetically
        
        # Output the folders in JSON format for VS Code tasks.json
        if len(sys.argv) > 1 and sys.argv[1] == "--json":
            # Output as JSON array for direct use in tasks.json
            print(json.dumps(product_folders, indent=2))
        else:
            # Output as human-readable list
            print(f"Found {len(product_folders)} product folders:")
            for folder in product_folders:
                print(f"  - {folder}")
    
    except Exception as e:
        print(f"Error listing product folders: {e}", file=sys.stderr)
        return 1
    
    return 0

def find_project_root():
    """Find the project root directory (where README.md is located)"""
    current_dir = os.path.abspath(os.path.dirname(__file__))
    
    # Traverse up until we find README.md or hit the root
    while True:
        if os.path.exists(os.path.join(current_dir, "README.md")):
            return current_dir
        
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # Reached root
            # Fall back to assuming we start 2 levels down from project root
            return os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
        
        current_dir = parent_dir

if __name__ == "__main__":
    sys.exit(main()) 