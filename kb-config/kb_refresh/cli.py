#!/usr/bin/env python
"""
KB Article Refresh CLI

Command-line interface for the KB article refresh tool.
"""

import sys
import os

# Add parent directory to path for direct script execution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Since Python package names can't have hyphens, we use the importlib approach
import importlib.util
spec = importlib.util.spec_from_file_location("main", os.path.join(os.path.dirname(__file__), "main.py"))
kb_refresh_main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb_refresh_main)

if __name__ == "__main__":
    kb_refresh_main.main() 