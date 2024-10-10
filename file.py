import os
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from flask_cors import CORS

ALLOWED_EXTENSIONS = set(['pdf', 'doc', 'docs'])
UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Downloads'))
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1000 * 1000  # 500 MB
app.config['CORS_HEADER'] = 'application/json'

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/upload', methods=['POST', 'GET'])
def fileUpload():
    if request.method == 'POST':
        # file = request.files.getlist('files')
        file = request.files['files']
        filename = ""
        print(request.files, "....")
        for f in file:
            print(f.filename)
            filename = secure_filename(f.filename)
            print(allowedFile(filename))
            if allowedFile(filename):
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                return jsonify({'message': 'File type not allowed'}), 400
        return jsonify({"name": filename, "status": "success"})
    else:
        return jsonify({"status": "Upload API GET Request Running"})
    
if __name__ == '__main__':
    app.run(debug=True,port=8000)