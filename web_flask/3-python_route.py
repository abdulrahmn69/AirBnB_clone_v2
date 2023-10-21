#!/usr/bin/python3
"""
Script that starts a Flask web application.
Routes:
    prev +
    /python/<text>: display “Python ”,
    The default value of text is “is cool”
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
def python(text = "is cool"):
    """display python <text>!"""
    if (text):
        text = text.replace("_", " ")
    return f"python, {escape(text)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=5000)