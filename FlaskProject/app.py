from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def printHello(name):
    return "Hello , %s" % name