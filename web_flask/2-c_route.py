#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def text(text):
    text.replace('_', ' ')
    return  'C %s' % escape(text)


if __name__ == '__name__':
    app.run()