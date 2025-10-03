# 🚀 MdHTML - Markdown to HTML Transpiler

A powerful and efficient **Markdown to HTML transpiler** built with Python that converts Markdown files to beautifully styled HTML documents. Features both command-line interface and web-based conversion with a modern, responsive frontend.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **📝 Full Markdown Support**: Headers, paragraphs, lists, tables, code blocks, blockquotes, horizontal rules
- **🎨 Rich Formatting**: Bold, italic, strikethrough, inline code, links, and images
- **💻 Dual Interface**: Command-line tool and web-based converter
- **🌐 Modern Web UI**: Responsive Bootstrap-powered frontend with drag-and-drop file upload
- **🛠️ Custom Styling**: Beautiful default CSS styling with customizable colors
- **📱 Mobile Friendly**: Responsive design that works on all devices
- **🔧 Easy Deployment**: Ready for deployment with Procfile support

## 📋 Supported Markdown Elements

| Element | Support Status | Example |
|---------|---------------|---------|
| Headers (H1-H6) | ✅ Full Support | `# Title` |
| Paragraphs | ✅ Full Support | Regular text |
| Lists (UL/OL) | ✅ Full Support | `- Item` or `1. Item` |
| Tables | ✅ Full Support | `\| Col1 \| Col2 \|` |
| Code Blocks | ✅ Full Support | ````code```` |
| Inline Code | ✅ Full Support | `` `code` `` |
| Blockquotes | ✅ Full Support | `> Quote` |
| Links | ✅ Full Support | `[text](url)` |
| Headers (H1-H6) | ✅ Full Supports | ✅ Full Support | `![alt](url)` |
| Bold/Italic | ✅ Full Support | `**bold**` `*italic*` |
| Strikethrough | ✅ Full Support | `~~crossed out~~` |
| Horizontal Rules | ✅ Full Support | `---` |

## 🚀 Quick Start

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Transpiler-mdHTML-.git
   cd Transpiler-mdHTML-
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Command Line Usage

Convert a markdown file to HTML:
```bash
python main.py examples/input.md
```

Or run interactively:
```bash
python main.py
# Enter file path when prompted
```

### Web Interface Usage

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

3. **Upload and convert**
   - Drag and drop your `.md` file or click to select
   - Click "Convert" to generate HTML
   - Download your converted file instantly

## 📁 Project Structure

```
Transpiler-mdHTML-/
├── app.py                 # Flask web application
├── main.py               # Command-line entry point
├── parser.py             # Markdown parsing engine
├── converter.py          # HTML conversion logic
├── file_handler.py       # File I/O operations
├── requirements.txt      # Python dependencies
├── Procfile             # Deployment configuration
├── frontend/            # Web interface files
│   ├── index.html       # Main page
│   ├── styles.css       # Styling
│   ├── script.js        # Frontend logic
│   ├── download.js      # Download functionality
│   └── download.html    # Download page
├── examples/            # Sample files
│   └── input.md         # Example markdown
├── output/              # Generated HTML files
└── tests/               # Test suites
```

## 🛠️ Core Components

### `parser.py`
- Parses markdown text into structured tokens
- Handles inline formatting (bold, italic, code, links)
- Supports nested elements and complex structures

### `converter.py`
- Converts parsed tokens to clean HTML
- Applies custom CSS styling
- Handles semantic HTML structure

### Web Application (`app.py`)
- RESTful API for file conversion
- Handles file uploads and downloads
- Serves static frontend files

## 🎨 Customization

### Styling
The converter applies beautiful default styles in `converter.py`. You can customize:
- Colors and fonts
- Layout and spacing
- Code syntax highlighting
- Table designs

### Adding Features
The modular design makes it easy to extend:
1. Add new markdown elements in `parser.py`
2. Implement conversion logic in `converter.py`
3. Update the frontend in `frontend/`

## 🌐 Deployment

### Heroku Deployment
The project includes a `Procfile` for easy Heroku deployment:
```bash
git push heroku main
```

### Local Production
```bash
python app.py
```

The application will be available at `transpiler-md-html.vercel.app`

## 📊 Example Conversion

**Input Markdown:**
```markdown
# My Document
## Subtitle

This is **bold text** and *italic text*.

- List item 1
- List item 2

> This is a blockquote

`inline code` and:

```python
def hello():
    print("Hello, World!")
```

| Name | Age |
|------|-----|
| John | 25  |
```

**Output HTML:**
Clean, semantic HTML with embedded CSS styling, maintaining all formatting and structure.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Built with Python and Flask
- Frontend powered by Bootstrap
- Inspired by popular markdown processors
- Special thanks to the open-source community

## 📞 Support

- 📧 Email: your-email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/Mohitbohra18/Transpiler-mdHTML-/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/Mohitbohra18/Transpiler-mdHTML-/discussions)

---

