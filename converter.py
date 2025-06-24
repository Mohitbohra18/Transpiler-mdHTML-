STYLE = """
<style>
    body {
        font-family: Arial, sans-serif;
        max-width: 800px;
        margin: auto;
        padding: 2rem;
        background: #f9f9f9;
        color: #333;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #2c3e50;
        margin-top: 1.2em;
    }
    code {
        background-color: #eee;
        padding: 2px 5px;
        border-radius: 4px;
        font-family: monospace;
    }
    pre {
        background-color: #272822;
        color: #f8f8f2;
        padding: 1em;
        border-radius: 6px;
        overflow-x: auto;
    }
    blockquote {
        border-left: 4px solid #ccc;
        padding-left: 1em;
        margin-left: 0;
        color: #555;
        font-style: italic;
    }
    ul, ol {
        margin-left: 2em;
    }
    hr {
        border: none;
        border-top: 1px solid #ccc;
        margin: 2em 0;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 1em 0;
    }
    table, th, td {
        border: 1px solid #ccc;
    }
    th, td {
        padding: 0.5em;
        text-align: left;
    }
    a {
        color: #3498db;
        text-decoration: none;
    }
</style>
"""

import re

def convert_inline(text):
    """Convert inline markdown formatting to HTML"""
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', text)  # Images
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)       # Links
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)                    # Inline code
    text = re.sub(r'\*\*(.*?)\*\*|__(.*?)__', r'<strong>\1\2</strong>', text)  # Bold
    text = re.sub(r'\*(.*?)\*|_(.*?)_', r'<em>\1\2</em>', text)                # Italic
    text = re.sub(r'~~(.*?)~~', r'<del>\1</del>', text)                        # Strikethrough
    return text

def convert_tokens_to_html(tokens):
    html = ["<html>", "<head>", "<meta charset='UTF-8'>", STYLE, "</head>", "<body>"]
    in_ol = False
    in_ul = False
    table_started = False

    for token_type, content in tokens:
        if token_type.startswith("h"):
            level = token_type[1]
            html.append(f"<h{level}>{content}</h{level}>")

        elif token_type == "p":
            html.append(f"<p>{content}</p>")

        elif token_type == "hr":
            html.append("<hr>")

        elif token_type == "blockquote":
            html.append(f"<blockquote>{content}</blockquote>")

        elif token_type == "code_block":
            html.append(f"<pre><code class='{content['lang']}'>{content['content']}</code></pre>")

        elif token_type == "ol_item":
            if not in_ol:
                html.append("<ol>")
                in_ol = True
            html.append(f"<li>{content}</li>")

        elif token_type == "ul_item":
            if not in_ul:
                html.append("<ul>")
                in_ul = True
            html.append(f"<li>{content}</li>")

        elif token_type == "table_row":
            if not table_started:
                html.append("<table>")
                table_started = True
            cols = [col.strip() for col in content.strip('|').split('|')]
            tag = "th" if "---" in content else "td"
            html.append("<tr>" + "".join(f"<{tag}>{col}</{tag}>" for col in cols) + "</tr>")

        else:
            html.append(f"<p>{content}</p>")

    if in_ol:
        html.append("</ol>")
    if in_ul:
        html.append("</ul>")
    if table_started:
        html.append("</table>")

    html.append("</body></html>")
    return "\n".join(html)
