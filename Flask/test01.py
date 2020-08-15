from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/hi')
def hi():
    return 'How are you!'
@app.route('/index')
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s</h1>'%name
def index():
    return '<h1>Hello Flash</h1>'
if __name__ == '__main__':
    app.run()