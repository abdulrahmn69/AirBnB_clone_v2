#!/usr/bin/python3
"""
Script that starts a Flask web application:
Routes:
    /states: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage
    sorted by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>
    /states/<id>: display a HTML page: (inside the tag BODY)
    If a State object is found with this id:
    H1 tag: “State: ”
    H3 tag: “Cities:”
    UL tag: with the list of City objects linked to the
    State sorted by name (A->Z)
    LI tag: description of one City: <city.id>: <B><city.name></B>
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States."""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
