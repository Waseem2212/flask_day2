import os
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['pdf', 'doc', 'docs'])
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file():
    file = request.files['files']
    # file = request.files['files']

    if file :
        filename = file

        file.save(os.path.join(app.config([UPLOAD_FOLDER], filename)))
        return "file upload succesfully"
    else:
        "no file upload"


if __name__ == '__main__':
    app.run(debug=True,port=8181)