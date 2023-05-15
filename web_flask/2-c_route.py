#!/usr/bin/python3
"""Flask"""
from flask import Flask
app = Flask(__name__)
app.url_map.merge_slashes = False


@app.route('/')
def hello_route():
    """Hello"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """hbnb"""
    return "HBNB"


@app.route('/c/<text>')
def text(text):
    """C route"""
    text = text.replace('_', ' ')
    return "C %s" % text


if __name__ == "__main__":
    app.run()
