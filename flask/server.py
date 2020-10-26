""" 1st simple flask server"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    """hello world entry"""
    return 'Hello World'


if __name__ == '__main__':
    app.run()
