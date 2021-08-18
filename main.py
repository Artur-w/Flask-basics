from flask import Flask # import flask class
from flask import jsonify # make output JSON serializable

app = Flask(__name__) # create an instance of the class

@app.route('/hello', methods=['GET', 'POST'])
# route() decorator tell Flask what URL should trigger the function
# methods specify which HTTP methods are allowed.
def welcome():
    return "Hello World!"

# Variable rules

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name

# JSON Serializable output

@app.route('/person/')
def helloj():
    return jsonify({'name':'Artur',
    'address':'Ireland'})

# use jsonify to automatically serialize list and tuples to JSON response
@app.route('/numbers/')
def print_list():
    return jsonify(list(range(5)))

# Redirection behaviour

@app.route('/home/')
def home():
    return "Home Page"

@app.route('/contact') # missing trailing slash
def contact():
    return "Contact Page"

'''
In the above example, the URL for the home endpoint has a trailing slash whereas the URL for the contact endpoint is missing the trailing slash.
This results in two different behaviours:
For the home endpoint, if you access the URL without the trailing slash, then Flask redirects you to the URL with the trailing slash.
For the contact endpoint, if you access the URL with the trailing slash, then it will result in status 404 Not Found.

'''

# Return Status code

@app.route('/teapot/')
def teapot():
    # return text below with status code 418 instead of 200
    return "Would you like some tea?", 418

# Before request
# we can specify a function which should execute before the request

@app.before_request
def before():
    print("This is executed BEFORE each request.")


# __name__ special variable in Python - takes the value of the script name
# it make sure the app runs only when executed in main file and not when it is imported in some other file.
if __name__ == '__main__':
    # run the Flask application
    # host is localhost or 127.0.0.1
    # 0.0.0.0 means all IPv4 addresses on the local machine
    # ensures that the server will be reachable from all addresses.
    app.run(host='0.0.0.0', port=105)