from flask import Flask, request, jsonify
import os
import base64

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    with open(file_path, 'rb') as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode('utf-8')

    return jsonify({'filename': file.filename, 'base64': encoded_string}), 200

if __name__ == '__main__':
    app.run(debug=True,port=3100)
