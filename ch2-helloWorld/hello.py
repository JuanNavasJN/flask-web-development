from flask import Flask, request
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/') 
def index():
    return '<h1>Hello World!</h1>' 

@app.route('/info') 
def info():
    user_agent = request.headers.get('User-Agent') 
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/user/<name>') 
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()
    