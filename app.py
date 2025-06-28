from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from parser import parse_markdown
from converter import convert_tokens_to_html
from file_handler import read_markdown_file, write_html_file

app = Flask(__name__, static_folder='frontend')
CORS(app)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'

# Create necessary directories
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Serve index.html on root route
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Serve all static frontend files (CSS, JS, etc.)
@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)

# Handle Markdown file upload and conversion
@app.route('/convert', methods=['POST'])
def convert_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not file.filename.endswith('.md'):
        return jsonify({'error': 'Only markdown files are supported'}), 400

    try:
        # Save the uploaded file
        filename = secure_filename(file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(input_path)

        # Read and convert the file
        md_text = read_markdown_file(input_path)
        tokens = parse_markdown(md_text)
        html = convert_tokens_to_html(tokens)

        # Save the converted HTML
        output_filename = os.path.splitext(filename)[0] + '.html'
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        write_html_file(OUTPUT_FOLDER, output_filename, html)

        # Clean up the uploaded file
        os.remove(input_path)

        return jsonify({
            'success': True,
            'filename': output_filename,
            'download_url': f'/download/{output_filename}'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Allow users to download the converted HTML
@app.route('/download/<filename>')
def download_file(filename):
    try:
        file_path = os.path.join(OUTPUT_FOLDER, filename)

        if not os.path.exists(file_path):
            return jsonify({'error': 'File not found'}), 404

        return send_file(
            file_path,
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Optional: if you have a static download.html page
@app.route('/download.html')
def download_html():
    return app.send_static_file('download.html')


# Run the app (Render may assign a dynamic port)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
