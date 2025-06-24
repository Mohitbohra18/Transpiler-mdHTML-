import os
import sys
from file_handler import read_markdown_file, write_html_file
from parser import parse_markdown
from converter import convert_tokens_to_html

def main():
    # 📥 Step 1: Get input file path (Interactive method)
    if len(sys.argv) < 2:
        input_path = input("⚠️ Please enter the path to the markdown file (e.g., examples/sample.md): ")
    else:
        input_path = sys.argv[1]

    # Debugging: Print the input path
    print(f"✅ Input path received: {input_path}")

    if not input_path.endswith(".md"):
        print("❌ Only markdown (.md) files are supported.")
        return

    try:
        # 📤 Step 2: Read markdown file
        md_text = read_markdown_file(input_path)
        
        # Check if the file content is read properly
        if not md_text:
            raise ValueError("❌ The file is empty or could not be read.")

        # 🧠 Step 3: Parse markdown to tokens
        tokens = parse_markdown(md_text)

        # 🛠️ Step 4: Convert tokens to HTML
        html = convert_tokens_to_html(tokens)

        # 💾 Step 5: Write output to HTML file
        filename = os.path.splitext(os.path.basename(input_path))[0] + ".html"
        write_html_file("output", filename, html)

        print("🚀 Conversion completed successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
