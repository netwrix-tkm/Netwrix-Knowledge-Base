#!/usr/bin/env python3
"""
Update VS Code tasks.json with the current list of product folders
"""

import os
import json
import sys
from pathlib import Path

def main():
    """Update the VS Code tasks.json file with the current list of product folders."""
    try:
        # Find the project root directory
        project_root = find_project_root()
        
        # Path to the tasks.json file
        tasks_json_path = os.path.join(project_root, ".vscode", "tasks.json")
        
        # Check if tasks.json exists
        if not os.path.exists(tasks_json_path):
            print(f"Error: tasks.json not found at {tasks_json_path}")
            return 1
        
        # Get the product folders
        from list_products import main as list_products_main
        
        # Temporarily redirect stdout to capture output
        import io
        from contextlib import redirect_stdout
        
        # Save original arguments
        original_argv = sys.argv.copy()
        
        # Set arguments for list_products.py
        sys.argv = [sys.argv[0], "--json"]
        
        # Capture the output
        f = io.StringIO()
        with redirect_stdout(f):
            list_products_main()
        
        # Restore original arguments
        sys.argv = original_argv
        
        # Get the product folders from captured output
        product_folders = json.loads(f.getvalue().strip())
        
        # Read the tasks.json file
        with open(tasks_json_path, "r", encoding="utf-8") as f:
            tasks_json = json.load(f)
        
        # Update the productFolder options
        for input_item in tasks_json.get("inputs", []):
            if input_item.get("id") == "productFolder":
                input_item["options"] = product_folders
        
        # Write the updated tasks.json file
        with open(tasks_json_path, "w", encoding="utf-8") as f:
            json.dump(tasks_json, f, indent=2)
        
        print(f"Updated tasks.json with {len(product_folders)} product folders")
        
    except Exception as e:
        print(f"Error updating tasks.json: {e}", file=sys.stderr)
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