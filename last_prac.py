import json                                                     
import os
from flask import Flask, request
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename

app = Flask(__name__)                                           


@app.route('/test_api',methods=['GET','POST'])            
def test_api():                                           
    uploaded_file = request.files['pdf']
    data = json.load(request.files['data'])
    filename = secure_filename(uploaded_file.filename)
    uploaded_file.save(os.path.join('C:\Users\Axix Technologies\Documents\files', filename))
    print(data)
    return 'success'

if __name__ == '__main__':
    app.run(debug=True, port=8080)






















# write code not include frontend all code of backend  of upload pdf,doc,docs file in flask and testing in postman