import re

def apply_inline_formatting(text):
    # Inline code: `code`
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)

    # Strikethrough: ~~text~~
    text = re.sub(r'~~(.+?)~~', r'<del>\1</del>', text)

    # Bold Italic (***text*** or ___text___)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'___(.+?)___', r'<strong><em>\1</em></strong>', text)

    # Bold (**text** or __text__)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)

    # Italic (*text* or _text_)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'(?<!_)_(?!_)(.+?)(?<!_)_(?!_)', r'<em>\1</em>', text)

    # Links: [text](url)
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)

    return text

def parse_markdown(md_text):
    lines = md_text.splitlines()
    tokens = []
    in_code_block = False
    code_block_lang = ''
    buffer = []

    for line in lines:
        line = line.rstrip()

        # Code block start or end
        if line.startswith("```"):
            if not in_code_block:
                in_code_block = True
                code_block_lang = line.strip("`").strip()
                buffer = []
            else:
                in_code_block = False
                tokens.append(("code_block", {
                    "lang": code_block_lang,
                    "content": "\n".join(buffer)
                }))
                buffer = []
            continue

        if in_code_block:
            buffer.append(line)
            continue

        # Headings
        if re.match(r"#{1,6} ", line):
            level = len(line.split(' ')[0])
            content = line[level+1:].strip()
            content = apply_inline_formatting(content)
            tokens.append((f"h{level}", content))
            continue

        # Horizontal Rule
        if re.match(r"^(-{3,}|_{3,}|\*{3,})$", line):
            tokens.append(("hr", None))
            continue

        # Blockquote
        if line.startswith("> "):
            content = apply_inline_formatting(line[2:].strip())
            tokens.append(("blockquote", content))
            continue

        # Ordered list
        if re.match(r"^\d+\.\s+", line):
            item = re.sub(r"^\d+\.\s+", '', line)
            item = apply_inline_formatting(item)
            tokens.append(("ol_item", item))
            continue

        # Unordered list
        if re.match(r"^[-+*]\s+", line):
            item = re.sub(r"^[-+*]\s+", '', line)
            item = apply_inline_formatting(item)
            tokens.append(("ul_item", item))
            continue

        # Table row
        if "|" in line:
            if re.match(r"^\s*\|.*\|\s*$", line):
                tokens.append(("table_row", line.strip()))
                continue

        # Paragraph or inline content
        if line.strip() != "":
            content = apply_inline_formatting(line.strip())
            tokens.append(("p", content))

    return tokens
