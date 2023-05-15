#!/usr/bin/python3
"""Flask

    Returns:
        text: loads a basic text to html
            through the route /c/<text> 
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_HBNB():
    """hello

    Returns:
        text: hello hbnb
    """
    return 'Hello HBNB'

@app.route('/hbnb')
def hbnb():
    """hbnb"""
    return 'HBNB'

