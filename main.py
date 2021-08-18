from flask import Flask # import flask class
from flask import jsonify # make output JSON serializable
from flask import request

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
    # Accessing Request Data
    # from flask import request
    data = request.data # access incoming request data as string
    args = request.args # access the parsed URL parameters. Returns ImmutableMultiDict
    form = request.form # access the form parameters. Return ImmutableMultiDict
    values = request.values # Retrurn CombinedMultiDict - combines args anmd form
    json = request.json # Return parsed JSON data if mimetype is application/json
    files = request.files # return MultiDict object which contains all uploaded files each key is the name of the fiule and value is the FileStorage object.
    auth = request.authorization # return an object of Authorization class. It represents an Authorization header sent by the client.
    print(f"{data}\n{args}\n{form}\n{values}\n{json}\n{files}\n{auth}\n")



# Logging
app.logger.debug('This is a DEBUG message')
app.logger.info('This is an INFO message')
app.logger.warning('This is a WARNING message')
app.logger.error('This is an ERROR message')

# __name__ special variable in Python - takes the value of the script name
# it make sure the app runs only when executed in main file and not when it is imported in some other file.
if __name__ == '__main__':
    # run the Flask application
    # host is localhost or 127.0.0.1
    # 0.0.0.0 means all IPv4 addresses on the local machine
    # ensures that the server will be reachable from all addresses.
    app.run(host='0.0.0.0', port=105)

'''
`app.run()` parameters
`app.run()` run the application on the server.
debug = True - automaticallt reload on code changes and show an interctive debugger in case of unhelded exceptions.
use_reloader = True - the server will automatically restart when code changes
threaded = True - the process will handle each request in a separate thread.
ssl_context → SSL Context for the connection. Expects ssl.SSLContext , a tuple in the form (cert_file, pkey_file) , or the string 'adhoc' if the server should automatically create the context. Default is None i.e. SSL is disabled.
This is used when we want to host the Flask application on HTTPS instead of HTTP.

'''