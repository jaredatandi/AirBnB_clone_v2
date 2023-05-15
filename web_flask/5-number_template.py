#!/usr/bin/python3
"""Flask"""


from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """hello"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    f_text = text.replace('_', ' ')
    return "C %s" % f_text


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def defaults_p(text):
    f_text2 = text.replace('_', ' ')
    return "Python %s" % f_text2


@app.route('/number/<int:n>')
def check_number(n):
    if isinstance(n, int):
        return "%d is a number" % n


@app.route('/number_template/<int:n>')
def number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run()
