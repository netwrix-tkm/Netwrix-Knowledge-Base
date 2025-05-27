#!/usr/bin/env python
"""
Simple wrapper script to run KB Article Refresh tool.
"""

import os
import sys
import importlib.util

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Import main from main.py in the current directory
spec = importlib.util.spec_from_file_location(
    "main", 
    os.path.join(script_dir, "main.py")
)
main_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(main_module)

if __name__ == "__main__":
    # Run the main function
    main_module.main() 