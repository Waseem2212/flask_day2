import json
from flask import Flask,request,jsonify

app = Flask(__name__)

employees = [
    {'id': 1,'name':'waseem'},{'id': 2,'name':'husnain'},{'id': 3,'name':'abdullah'}
]
# @app.route('/employees')
# @app.route('/',methods=['GET'])
# def get_employees():
#     return jsonify(employees)
@app.route('/employees', methods=['GET'])
def get_employees():
 return jsonify(employees)

@app.route('/create-employees',methods=['POST'])
def create_employee():
    global nextEmployeeId
    employee = json.loads(request.data)
    # if not employee_is_valid(employee):
    #     return jsonify({'error':'Invalid employee properties'}),400
    
    employee['id'] = nextEmployeeId
    nextEmployeeId +=1
    employees.append(employee)

    return '',201, {'location':f'/employees/{employee["id"]}'}


if __name__ == '__main__':
    app.run(debug=True,port=8000)