from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = set(['pdf', 'csv', 'png', 'jpeg', 'jpg'])
UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Downloads'))
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 500 * 1000 * 1000  # 500 MB
app.config['CORS_HEADER'] = 'application/json'

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file', methods=['POST', 'GET'])
def fileUpload():
    if request.method == 'POST':
        file = request.files.getlist('files')
        filename = ""
        if allowedFile(filename):
                filename.save(os.path.join(app.config['UPLOAD_FOLDER'], filename                                  ))
        else:
                return jsonify({'message': 'File type not allowed'}), 400
    return jsonify({"name": filename, "status": "success"})

if __name__ == '__main__':
    app.run(debug=True,port=3000)