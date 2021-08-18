from flask import Flask # import flask class

app = Flask(__name__) # create an instance of the class

@app.route('/hello', methods=['GET', 'POST'])
# route() decorator tell Flask what URL should trigger the function
# methods specify which HTTP methods are allowed.
def welcome():
    return "Hello World!"

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name



# __name__ special variable in Python - takes the value of the script name
# it make sure the app runs only when executed in main file and not when it is imported in some other file.
if __name__ == '__main__':
    # run the Flask application
    # host is localhost or 127.0.0.1
    # 0.0.0.0 means all IPv4 addresses on the local machine
    # ensures that the server will be reachable from all addresses.
    app.run(host='0.0.0.0', port=105)