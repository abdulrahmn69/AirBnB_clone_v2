#!/usr/bin/python3
"""
Script that starts a Flask web application.
Routes:
    prev +
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
"""
from flask import Flask, render_template
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberTemp(n):
    """display HTML page <n>!"""
    if n.__class__ is int:
        return render_template("5-number.html", theNumber=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddEven(n):
    """display a HTML page odd-even"""
    if n.__class__ is int:
        return render_template("6-number_odd_or_even.html", theNumber=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
