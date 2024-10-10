from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/api/signup', methods=['POST'])

def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')


    return jsonify({
        "name":name,
        "email":email,
        "password":password
    })


@app.route('/api/signin', methods=['POST'])
def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email == data.get('email') and password == data.get('password'):
        return jsonify({'message':'Login Successfull'})
    else:
         return jsonify({'message':'email and password are incorrect'})
        

if __name__ == '__main__':
    app.run(debug=True,port=8383)