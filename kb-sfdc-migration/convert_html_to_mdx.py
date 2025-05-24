import os
import argparse
from pathlib import Path
import re
import html
import html2markdown

# Adapted clean_html function
def clean_html(html_content_param):
    """Clean up HTML content before conversion"""
    # Remove the content of <title> tags first
    html_content_param = re.sub(r'<title[^>]*>.*?</title>', '', html_content_param, flags=re.IGNORECASE | re.DOTALL)

    if not html_content_param: # Replaced pd.isna
        return ""
    
    html_text_content = html_content_param # Use a distinct variable name for modifications

    # Remove script and style tags completely
    html_text_content = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', html_text_content, flags=re.IGNORECASE | re.DOTALL)
    html_text_content = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', html_text_content, flags=re.IGNORECASE | re.DOTALL)
    
    # Handle headers (h1-h6)
    for i in range(1, 7):
        html_text_content = re.sub(
            f'<h{i}[^>]*>(.*?)</h{i}>',
            lambda m: f'\n\n{"#" * i} {m.group(1).strip()}\n\n',
            html_text_content,
            flags=re.IGNORECASE | re.DOTALL
        )
    
    # Handle code blocks - preserve them before general HTML processing
    def process_code_block(match):
        full_match = match.group(0)
        if '<code' in full_match.lower() and '</code>' in full_match.lower():
            code_match_obj = re.search(r'<code[^>]*>(.*?)<\/code>', full_match, flags=re.DOTALL | re.IGNORECASE) 
            if code_match_obj:
                code_content_str = code_match_obj.group(1).strip() 
                code_content_str = html.unescape(code_content_str)
                code_content_str = re.sub(r'<[^>]+>', '', code_content_str)
                return f'\n```\n{code_content_str}\n```\n'
        if full_match.lower().startswith('<pre'):
            pre_content_str = re.sub(r'<pre[^>]*>', '', full_match, flags=re.IGNORECASE) 
            pre_content_str = re.sub(r'<\/pre>', '', pre_content_str, flags=re.IGNORECASE)
            pre_content_str = html.unescape(pre_content_str).strip()
            pre_content_str = re.sub(r'<[^>]+>', '', pre_content_str)
            if '\n' in pre_content_str:
                return f'\n```\n{pre_content_str}\n```\n'
            return f'\n{pre_content_str}\n'
        content_text = re.sub(r'<[^>]+>', '', full_match) 
        return f'\n{html.unescape(content_text).strip()}\n'
    
    html_text_content = re.sub(
        r'<pre[^>]*>\s*<code[^>]*>(.*?)</code>\s*</pre>',
        process_code_block,
        html_text_content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    html_text_content = re.sub(r'<br\s*/?>', '  \n', html_text_content, flags=re.IGNORECASE)
    
    def handle_remaining_pre(match):
        pre_content_str = match.group(1).strip() 
        if pre_content_str and '```' not in pre_content_str:
            return f'\n```\n{pre_content_str}\n```\n'
        return f'\n{pre_content_str}\n'
    
    html_text_content = re.sub(r'<pre[^>]*>(.*?)</pre>', handle_remaining_pre, html_text_content, flags=re.IGNORECASE | re.DOTALL)
        
    html_text_content = re.sub(r'\n{3,}', '\n\n', html_text_content)
    html_text_content = re.sub(r' +', ' ', html_text_content)
    
    def process_divs(html_text_arg): 
        def protect_list(match):
            content_text = match.group(1) 
            if '<li>' in content_text.lower() or '<ul>' in content_text.lower() or '<ol>' in content_text.lower():
                return content_text
            return f'\n{content_text}\n'
        
        processed_html_text = re.sub( 
            r'<div[^>]*>(.*?)</div>',
            protect_list,
            html_text_arg,
            flags=re.IGNORECASE | re.DOTALL
        )
        processed_html_text = re.sub(r'<div[^>]*>', '\n', processed_html_text, flags=re.IGNORECASE)
        processed_html_text = processed_html_text.replace('</div>', '\n')
        return processed_html_text
    
    html_text_content = process_divs(html_text_content)
    
    html_text_content = re.sub(r'<p[^>]*>', '\n\n', html_text_content, flags=re.IGNORECASE)
    html_text_content = html_text_content.replace('</p>', '\n\n')
    
    def process_list_item_sub_func(match): 
        item_content_str = match.group(1).strip() 
        if not item_content_str or item_content_str.isspace():
            return '\n'
        item_content_str = re.sub(r'<[^>]+>', '', item_content_str) # Remove tags from list item content
        item_content_str = re.sub(r'\s+', ' ', item_content_str).strip()
        parent_tag_str = '' 
        if match.lastindex is not None and match.lastindex > 1: # Check if group 2 exists
            parent_tag_str = match.group(2).lower() if match.group(2) else ''
        indent_str = '    ' if parent_tag_str in ('ol', 'ul') else '' 
        return f'\n{indent_str}* {item_content_str}\n'

    def process_nested_lists(html_text_arg): 
        def process_whole_list(match):
            list_items_str = match.group(2) 
            list_items_str = re.sub(
                r'([.!?])\s*([A-Z])', 
                lambda m: f'{m.group(1)}\n* {m.group(2).lower()}', 
                list_items_str
            )
            list_items_str = re.sub(
                r'<li[^>]*>(.*?)</li>',
                lambda m: f'\n* {re.sub(r"<[^>]+>", "", m.group(1)).strip()}\n', # Strip tags from li content here too
                list_items_str,
                flags=re.IGNORECASE | re.DOTALL
            )
            list_items_str = re.sub(r'\n\*\s*\n', '\n', list_items_str)
            return f'\n{list_items_str}\n'
        
        processed_html_text = re.sub( 
            r'<(ul|ol)[^>]*>(.*?)</\1>',
            process_whole_list,
            html_text_arg,
            flags=re.IGNORECASE | re.DOTALL
        )
        processed_html_text = re.sub(
            r'(\d+\.\s*[^\n.]+)(?=\s+\d+\.|$)',
            lambda m: f'\n* {m.group(1).strip()}\n',
            processed_html_text
        )
        processed_html_text = re.sub(
            r'([^\n])(\s*-\s*)([^\n]+)(?=\s+-|$)',
            lambda m: f'{m.group(1)}\n* {m.group(3).strip()}\n',
            processed_html_text
        )
        return processed_html_text
    
    html_text_content = process_nested_lists(html_text_content)
    
    html_text_content = re.sub(
        r'<li[^>]*>(.*?)</li>', # This regex does not have group 2 for parent_tag
        process_list_item_sub_func, 
        html_text_content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    html_text_content = re.sub(r'</?[ou]l[^>]*>', '\n', html_text_content, flags=re.IGNORECASE) 
    html_text_content = re.sub(r'\n\*\s*\n', '\n\n', html_text_content) 
    html_text_content = re.sub(r'([.!?])\s*([A-Z])', lambda m: f'{m.group(1)}\n\n{m.group(2)}', html_text_content)
    html_text_content = re.sub(r'(\n\* [^\n]+?)\.\s*([A-Z])', lambda m: f'{m.group(1)}.\n\n{m.group(2).lower()}', html_text_content)
    html_text_content = re.sub(r'([^\n])(\n\* )', r'\1\n\2', html_text_content)
    html_text_content = re.sub(r'(\n\* [^\n]*)\n([^\n*])', r'\1\n\n\2', html_text_content)
    html_text_content = re.sub(r'(\n\* [^\n]*)(\n\* )', r'\1\2', html_text_content)
    
    html_text_content = re.sub(
        r'(For (?:Windows|macOS) operating systems:)\s*([^\n]+)',
        lambda m: f'### {m.group(1)}\n\n{m.group(2).strip()}',
        html_text_content,
        flags=re.IGNORECASE
    )
    for pattern in [
        (r'(In the [^:]+:)([^\n]+)', r'\1\n\n\2'),
        (r'(Click|Select|Verify|Ensure|Attempt to|Navigate to)([^\n]+?)(?=\s+[A-Z][a-z]|$)', r'* \1\2\n'),
    ]:
        html_text_content = re.sub(pattern[0], pattern[1], html_text_content, flags=re.IGNORECASE)
    
    html_text_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_text_content, flags=re.IGNORECASE | re.DOTALL)
    
    def process_links(html_text_arg): 
        processed_html_text = re.sub( 
            r'<a\s+(?:[^>]*?\s+)?href=(["\'])(.*?)\1[^>]*>(.*?)</a>',
            lambda m: f'[{m.group(3).strip()}]({m.group(2).strip()})',
            html_text_arg,
            flags=re.IGNORECASE | re.DOTALL
        )
        processed_html_text = re.sub(
            r'<a\s+[^>]*?href=(["\'])(.*?)\1[^>]*>(.*?)</a>', 
            lambda m: f'[{m.group(3).strip()}]({m.group(2).strip()})',
            processed_html_text,
            flags=re.IGNORECASE | re.DOTALL
        )
        return processed_html_text
    
    html_text_content = process_links(html_text_content)
    html_text_content = re.sub(r'<[^>]+>', '', html_text_content) # Final cleanup of any remaining tags
    return html_text_content.strip()

# Adapted convert_html_to_markdown function
def convert_html_to_markdown(html_content_str):
    """Convert HTML to markdown using html2markdown with custom handling"""
    if not html_content_str: 
        return ""
    
    try:
        clean_content = clean_html(html_content_str) 
        markdown = html2markdown.convert(clean_content)
        markdown = markdown.lstrip('\n') 
        markdown = html.unescape(markdown)
        markdown = re.sub(r'\n{3,}', '\n\n', markdown).strip() # Correct processing
        return markdown
    except Exception as e:
        print(f"Error converting HTML to markdown: {e}")
        return str(html_content_str) # Return original content on error

def find_html_files(input_dir_path: str): # Parameter name from spec
    """
    Finds all HTML files (files ending with .html) within a given input directory and its subdirectories.
    """
    input_dir_path_obj = Path(input_dir_path) # Convert string to Path object
    if not input_dir_path_obj.is_dir():
        return []
    return list(input_dir_path_obj.rglob('*.html'))

def main():
    parser = argparse.ArgumentParser(description="Convert HTML files to MDX.")
    parser.add_argument("input_dir", type=str, help="Input directory containing HTML files.")
    parser.add_argument("output_dir", type=str, help="Output directory for MDX files.")
    args = parser.parse_args()

    html_files = find_html_files(args.input_dir)

    if not html_files:
        return

    for html_file_path in html_files:
        try:
            # Defined inside loop as per spec
            input_dir_path_obj_loop = Path(args.input_dir) 
            output_dir_path_obj_loop = Path(args.output_dir) 
            
            relative_path = html_file_path.relative_to(input_dir_path_obj_loop)
            output_file_path = output_dir_path_obj_loop.joinpath(relative_path).with_suffix('.mdx')
            
            output_file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(html_file_path, "r", encoding="utf-8", errors="replace") as f: 
                html_data_content = f.read()

            title_match = re.search(r'<title[^>]*>([^<]+)</title>', html_data_content, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip()
            else:
                title = html_file_path.stem
            title = title.replace('"', '\\"') 

            desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html_data_content, re.IGNORECASE)
            description = desc_match.group(1).strip().replace('"', '\\"') if desc_match else None
            
            keywords_match = re.search(r'<meta\s+name="keywords"\s+content="([^"]+)"', html_data_content, re.IGNORECASE)
            keywords = keywords_match.group(1).strip().replace('"', '\\"') if keywords_match else None

            markdown_body = convert_html_to_markdown(html_data_content)

            frontmatter_parts = ["---", f'title: "{title}"']
            if description:
                frontmatter_parts.append(f'description: "{description}"')
            if keywords:
                frontmatter_parts.append(f'keywords: "{keywords}"')
            frontmatter_parts.append("---")
            frontmatter_content = "\n".join(frontmatter_parts) + "\n\n"
            
            final_mdx_content = frontmatter_content + markdown_body

            with open(output_file_path, "w", encoding="utf-8") as f: 
                f.write(final_mdx_content)
            
            print(f"Processing {html_file_path} -> {output_file_path}")

        except Exception as e:
            print(f"Error processing file {html_file_path}: {e}")
            continue

if __name__ == "__main__":
    main()
