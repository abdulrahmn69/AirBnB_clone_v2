#!/usr/bin/python3
"""
Script that starts a Flask web application.
Routes:
    prev +
    /number/<n>: display “n is a number”
    only if n is an integer
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display Hello HBNB!"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display C <text>!"""
    text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python(text="is cool"):
    """display python <text>!"""
    if (text):
        text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display <n> is a number"""
    if n.__class__ is int:
        return f"{escape(n)} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
