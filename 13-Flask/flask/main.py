from flask import Flask
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return '<html><head><title>Welcome</title></head><body><h1>Welcome to this Flask best Application!</h1></body></html>'

@app.route('/index')
def index():
    return 'Welcome to Index!'

if __name__ == "__name__":
    app.run(debug=True)
