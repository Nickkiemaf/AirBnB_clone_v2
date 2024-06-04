#!/usr/bin/python3
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route '/' to display 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Route '/hbnb' to display 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """Route '/c/<text>' to display 'C ' followed by the value of the text variable."""
    return "C {}".format(escape(text.replace("_", " ")))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    """Route '/python/<text>' to display 'Python ' followed by the value of the text variable."""
    return "Python {}".format(escape(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Route '/number/<n>' to display 'n is a number' if n is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
