#!/usr/bin/python3
"""
Script that starts a Flask web application.
Routes:
    prev +
    /number_template/<n>: display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
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
    return f"C, {escape(text)}"

@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python(text = "is cool"):
    """display python <text>!"""
    if (text):
        text = text.replace("_", " ")
    return f"python, {escape(text)}"

@app.route("/number/<text>", strict_slashes=False)
def number(text):
    """display <text> is a number"""
    if type(text) == int:
        return f"{escape(text)} is a number"

@app.route("/number_template/<n>", strict_slashes=False)
def numberTemp(n):
    """display HTML page <n>!"""
    return f"C, {escape(n)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=5000)