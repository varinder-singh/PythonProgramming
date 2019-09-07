from flask import Flask, jsonify, request
app = Flask(__name__)
empDB = [
    {
        'id': '101',
        'name': 'Saravanan S',
        'title': 'Technical Leader'
    },
    {
        'id': '201',
        'name': 'Rajkumar P',
        'title': 'Sr Software Engineer'
    }
]


@app.route("/")
def entry():
    return "The app is functional"

@app.route('/empDB/employee', methods=['GET'])
def getAllEmployees():
    return jsonify({'emps': empDB})


@app.route('/empDB/employee/<empId>', methods=['GET'])
def getEmployeeByEmpId(empId):
    print(request)
    usr = [emp for emp in empDB if (emp['id'] == empId)]
    return jsonify({'emp' : usr})


if __name__ == "__main__":
    app.run()