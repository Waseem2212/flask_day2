import os
from flask import Flask, jsonify, request
# from PyPDF2 import PdfFileReader, PdfFileWriter,PdfReader
import PyPDF2
app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['pdf', 'doc', 'docs'])
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):os.makedirs(UPLOAD_FOLDER)


def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])

def upload_file():
    if 'files' not in request.files:
        return jsonify({
            'error':'no file exist'
        })
    file = request.files['files']
    if file.filename == '':
       return jsonify({
            'error':'no selected file'
        })
    if file and allowedFile(file.filename):
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return  jsonify({
            'message':'file upload successfull : ' + filename
        })

@app.route('/read', methods=['POST'])
def file_upload():

    file = request.files.get('files')

    if not file:
        return 'No file uploaded.'

    pdfReader = PyPDF2.PdfReader(file)

    print(pdfReader.pages)
    pageObj = pdfReader.pages[0]
    print(pageObj.extract_text())

    return 'success'

if __name__ == '__main__':
    app.run(debug=True,port=8000)