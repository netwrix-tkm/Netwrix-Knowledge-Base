#!/bin/bash

# Script to update the VS Code tasks.json file with the current list of product folders

# Find the project root directory
PROJECT_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)

# Path to the tasks.json file
TASKS_JSON="${PROJECT_ROOT}/.vscode/tasks.json"

# Get the product folders as a JSON array
PRODUCT_FOLDERS=$("${PROJECT_ROOT}/.venv/Scripts/python" "${PROJECT_ROOT}/kb-tools/kb_evaluate/list_products.py" --json)

if [ $? -ne 0 ]; then
    echo "Error running list_products.py"
    exit 1
fi

# Check if tasks.json exists
if [ ! -f "$TASKS_JSON" ]; then
    echo "Error: tasks.json not found at $TASKS_JSON"
    exit 1
fi

# Create a temporary file
TMP_FILE=$(mktemp)

# Parse the tasks.json and update the "options" array for productFolder
jq --argjson new_options "$PRODUCT_FOLDERS" '.inputs[] |= if .id == "productFolder" then .options = $new_options else . end' "$TASKS_JSON" > "$TMP_FILE"

# Check if jq command was successful
if [ $? -ne 0 ]; then
    echo "Error processing tasks.json with jq"
    rm "$TMP_FILE"
    echo "You need to install 'jq' command: https://jqlang.github.io/jq/download/"
    exit 1
fi

# Copy the modified content back to the original file
cp "$TMP_FILE" "$TASKS_JSON"

# Clean up
rm "$TMP_FILE"

echo "Updated tasks.json with $(echo $PRODUCT_FOLDERS | jq 'length') product folders" 