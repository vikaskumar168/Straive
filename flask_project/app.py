from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/<name>')
def print_hello(name):
    return 'Hello ,%s' %name

@app.route('/add/<int:num1>/<int:num2>', methods=['GET'])
def add(num1, num2):
    return jsonify({'result': num1 + num2})

@app.route('/subtract/<int:num1>/<int:num2>', methods=['GET'])
def get_subtract(num1, num2):
    return jsonify({'operation': 'subtract', 'result': num1 - num2})

@app.route('/multiply/<int:num1>/<int:num2>', methods=['GET'])
def get_multiply(num1, num2):
    return jsonify({'operation': 'multiply', 'result': num1 * num2})

@app.route('/divide/<int:num1>/<int:num2>', methods=['GET'])
def get_divide(num1, num2):
    if num2 == 0:
        return jsonify({'error': 'Division by zero is not allowed'}), 400
    return jsonify({'operation': 'divide', 'result': num1 / num2})



# @app.route('/calculate', methods=['POST'])
# def calculate():
#     data = request.get_json()
#
#     if not data or 'num1' not in data or 'num2' not in data or 'operation' not in data:
#         return jsonify({'error': 'Please provide num1, num2, and operation'}), 400
#
#     num1 = data['num1']
#     num2 = data['num2']
#     operation = data['operation'].lower()
#
#     if operation == 'add':
#         result = num1 + num2
#     elif operation == 'subtract':
#         result = num1 - num2
#     elif operation == 'multiply':
#         result = num1 * num2
#     elif operation == 'divide':
#         if num2 == 0:
#             return jsonify({'error': 'Division by zero is not allowed'}), 400
#         result = num1 / num2
#     else:
#         return jsonify({'error': 'Unsupported operation'}), 400
#
#     return jsonify({'result': result})

if __name__ == '__main__':
    app.run()