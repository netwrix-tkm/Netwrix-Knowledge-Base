#!/usr/bin/env python3

import os
import sys
import argparse
import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    """Preprocess and clean text for comparison."""
    if not text:
        return ""
    # Remove HTML
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    # Remove non-alphanumeric, short words, extra spaces, etc.
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\b\w{1,2}\b', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text.lower()

def extract_title_content(html_path):
    """Extract title and clean content from HTML file."""
    with open(html_path, encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    title_tag = soup.find('h1') or soup.find('title')
    title = title_tag.get_text(strip=True) if title_tag else Path(html_path).name
    # Remove scripts, styles etc.
    for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside', 'meta', 'link']):
        element.decompose()
    content = ' '.join(soup.stripped_strings)
    return title, content

def collect_product_html_files(product_path: Path, exclude_file=None):
    """Collect all HTML article files in a given product subdirectory."""
    articles = []
    for html_file in product_path.glob("*.html"):
        if exclude_file and html_file.resolve() == Path(exclude_file).resolve():
            continue
        with open(html_file, encoding="utf-8") as f:
            content = f.read()
        title, _ = extract_title_content(html_file)
        articles.append({
            "title": title,
            "content": content,
            "path": str(html_file)
        })
    return articles

def find_duplicates(new_article, articles, threshold=0.8, top_n=5):
    all_texts = [clean_text(a['content']) for a in articles]
    if not all_texts:
        return []
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    new_text = clean_text(new_article['content'])
    input_vector = vectorizer.transform([new_text])
    similarities = cosine_similarity(input_vector, tfidf_matrix).flatten()
    duplicates = [
        {
            "title": articles[i]["title"],
            "path": articles[i]["path"],
            "similarity": float(similarities[i])
        }
        for i, sim in enumerate(similarities) if sim >= threshold
    ]
    return sorted(duplicates, key=lambda x: -x["similarity"])[:top_n]

def main():
    parser = argparse.ArgumentParser(description="Check KB article for duplicates in the repo.")
    parser.add_argument('--product-dir', required=True, help="Path to the product's KB HTML folder (e.g. 'kb-html/Activity Monitor')")
    parser.add_argument('--file', required=True, help="New article HTML to check (full path, must exist)")
    parser.add_argument('--threshold', type=float, default=0.8, help="Similarity threshold, default 0.8")
    parser.add_argument('--output-json', help="If set, write report to this JSON file")
    args = parser.parse_args()

    product_dir = Path(args.product_dir)
    if not product_dir.exists():
        print(f"ERROR: Product dir not found: {product_dir}", file=sys.stderr)
        sys.exit(2)
    if not Path(args.file).exists():
        print(f"ERROR: New article file not found: {args.file}", file=sys.stderr)
        sys.exit(2)

    # Extract new article
    title, content = extract_title_content(args.file)
    new_article = {"title": title, "content": content, "path": args.file}

    # Read others
    articles = collect_product_html_files(product_dir, exclude_file=args.file)
    duplicates = find_duplicates(new_article, articles, threshold=args.threshold)

    # Show results
    if duplicates:
        print(f"Found {len(duplicates)} potential duplicate(s) for '{title}':")
        for d in duplicates:
            print(f"  {d['path']} (similarity: {d['similarity']:.3f})")
        if args.output_json:
            with open(args.output_json, "w") as f:
                json.dump({"duplicates": duplicates}, f, indent=2)
        sys.exit(1)
    else:
        print(f"No duplicates found for '{title}'")
        if args.output_json:
            with open(args.output_json, "w") as f:
                json.dump({"duplicates": []}, f)
        sys.exit(0)

if __name__ == "__main__":
    main()
