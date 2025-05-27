#!/usr/bin/env python
"""
Setup script for KB Article Refresh tool.
"""

from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), "..", "requirements.txt")) as f:
    requirements = f.read().splitlines()

setup(
    name="kb-refresh",
    version="0.1.0",
    description="A tool for refreshing knowledge base articles using PDF documentation",
    author="Netwrix Support Team",
    package_dir={"kb_refresh": "kb-refresh"},
    packages=["kb_refresh"],
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "kb-refresh=kb_refresh.cli:main",
        ],
    },
    python_requires=">=3.8",
) 