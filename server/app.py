#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Index view
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string view
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print the parameter in the console
    return parameter  # Display the parameter in the web browser

# Count view
@app.route('/count/<int:parameter>')
def count(parameter):
    # Return numbers from 0 to parameter-1 with a trailing newline
    numbers = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return numbers  # Return the numbers as plain text

# Math view
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
