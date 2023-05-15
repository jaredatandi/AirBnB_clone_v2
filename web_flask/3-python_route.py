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


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    formatted_text = text.replace('_', " ")
    return "Python %s" % formatted_text


if __name__ == "__main__":
    app.run()
