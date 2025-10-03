# 🚀 MdHTML - Markdown to HTML Transpiler

A powerful and efficient **Markdown to HTML transpiler** built with Python that converts Markdown files to beautifully styled HTML documents.  
Features both a **command-line interface** and a **web-based converter** with a modern, responsive frontend.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## ✨ Features

- **📝 Full Markdown Support**: Headers, paragraphs, lists, tables, code blocks, blockquotes, horizontal rules  
- **🎨 Rich Formatting**: Bold, italic, strikethrough, inline code, links, and images  
- **💻 Dual Interface**: Command-line tool and web-based converter  
- **🌐 Modern Web UI**: Responsive Bootstrap-powered frontend with drag-and-drop file upload  
- **🛠️ Custom Styling**: Beautiful default CSS styling with customizable colors  
- **📱 Mobile Friendly**: Responsive design that works on all devices  
- **🔧 Easy Deployment**: Ready for deployment with Procfile support  

---

## 📋 Supported Markdown Elements

| Element        | Support | Example |
|----------------|----------|---------|
| Headers (H1–H6) | ✅ Full Support | `# Title` |
| Paragraphs      | ✅ Full Support | Regular text |
| Lists (UL/OL)   | ✅ Full Support | `- Item` / `1. Item` |
| Tables          | ✅ Full Support | `\| Col1 \| Col2 \|` |
| Code Blocks     | ✅ Full Support | ```` ```python ... ``` ```` |
| Inline Code     | ✅ Full Support | `` `code` `` |
| Blockquotes     | ✅ Full Support | `> Quote` |
| Links           | ✅ Full Support | `[text](https://example.com)` |
| Images          | ✅ Full Support | `![alt](url)` |
| Bold / Italic   | ✅ Full Support | `**bold**`, `*italic*` |
| Strikethrough   | ✅ Full Support | `~~crossed~~` |
| Horizontal Rule | ✅ Full Support | `---` |

---

## 🚀 Quick Start

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mohitbohra18/Transpiler-mdHTML-.git
   cd Transpiler-mdHTML-
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

### Command-Line Usage

Convert a Markdown file to HTML:

```bash
python main.py examples/input.md
```

Or run interactively:

```bash
python main.py
# Enter file path when prompted
```

---

### Web Interface Usage

1. **Start the Flask server**

   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000) (or your deployed URL: [https://transpiler-md-html.vercel.app](https://transpiler-md-html.vercel.app))

3. **Upload & Convert**

   * Drag and drop your `.md` file or click to select
   * Click **Convert** to generate HTML
   * Download your converted file instantly

---

## 📁 Project Structure

```
Transpiler-mdHTML-/
├── app.py              # Flask web application
├── main.py             # Command-line entry point
├── parser.py           # Markdown parsing engine
├── converter.py        # HTML conversion logic
├── file_handler.py     # File I/O operations
├── requirements.txt    # Python dependencies
├── Procfile            # Deployment configuration
├── frontend/           # Web interface files
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   ├── download.js
│   └── download.html
├── examples/           # Sample files
│   └── input.md
├── output/             # Generated HTML files
└── tests/              # Test suites
```

---

## 🛠️ Core Components

### `parser.py`

* Parses Markdown text into structured tokens
* Handles inline formatting (bold, italic, code, links)
* Supports nested elements and complex structures

### `converter.py`

* Converts parsed tokens to clean, semantic HTML
* Applies custom CSS styling
* Handles advanced Markdown features

### `app.py` (Web App)

* RESTful API for file conversion
* Handles file uploads & downloads
* Serves static frontend files

---

## 🎨 Customization

### Styling

Default styles are applied via `converter.py` & frontend CSS. You can easily modify:

* Colors, fonts, and themes
* Layout & spacing
* Code syntax highlighting
* Table designs

### Adding Features

1. Add parsing logic in `parser.py`
2. Extend conversion in `converter.py`
3. Update frontend in `frontend/`

---

## 🌐 Deployment

### Heroku Deployment

```bash
git push heroku main
```

### Local Deployment

```bash
python app.py
```

App will be available at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

Deployed version: [https://transpiler-md-html.vercel.app](https://transpiler-md-html.vercel.app)

---

## 📊 Example Conversion

**Input Markdown:**

````markdown
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
````

| Name | Age |
| ---- | --- |
| John | 25  |

````

**Output HTML (simplified):**
```html
<h1>My Document</h1>
<h2>Subtitle</h2>
<p>This is <strong>bold text</strong> and <em>italic text</em>.</p>
<ul>
  <li>List item 1</li>
  <li>List item 2</li>
</ul>
<blockquote>This is a blockquote</blockquote>
<p><code>inline code</code> and:</p>
<pre><code class="language-python">def hello():
    print("Hello, World!")</code></pre>
<table>
  <thead>
    <tr><th>Name</th><th>Age</th></tr>
  </thead>
  <tbody>
    <tr><td>John</td><td>25</td></tr>
  </tbody>
</table>
````

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to your branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

Licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

* Built with **Python** & **Flask**
* Frontend powered by **Bootstrap**
* Inspired by popular Markdown processors
* Thanks to the open-source community 💙

---

## 📞 Support

* 📧 Email: `manvendarbohra18@gmail.com`
* 🐛 [Report Issues](https://github.com/Mohitbohra18/Transpiler-mdHTML-/issues)
* 💬 [Start a Discussion](https://github.com/Mohitbohra18/Transpiler-mdHTML-/discussions)

---


