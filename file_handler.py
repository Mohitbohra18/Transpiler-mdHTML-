import os

def read_markdown_file(filepath):
    """Read markdown (.md) file and return content as string"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Input file not found: {filepath}")
    
    print(f"✅ Reading file: {filepath}")  # Debugging line to check file path
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"✅ File content read successfully.")  # Confirm file content is read
        return content

def write_html_file(output_dir, filename, html_content):
    """Write HTML content to output directory"""
    os.makedirs(output_dir, exist_ok=True)
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✅ HTML saved at: {full_path}")
