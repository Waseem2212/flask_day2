from flask import Flask, request, jsonify
import os
import PyPDF2
import docx

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
    return text

def read_docx(file_path):
    doc = docx.Document(file_path)
    text = '\n'.join(paragraph.text for paragraph in doc.paragraphs)
    return text

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        
        if file.filename.endswith('.pdf'):
            text = read_pdf(file_path)
        elif file.filename.endswith('.docx'):
            text = read_docx(file_path)
        else:
            return jsonify({'error': 'Unsupported file type'}), 400
        
        return jsonify({'filename': file.filename, 'content': text}), 200
    
    return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    app.run(debug=True,port=3000)
