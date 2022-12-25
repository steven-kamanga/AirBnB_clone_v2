#!/usr/bin/python3
"""Module: Starts a Flask web app and fetches data from storage engine"""
from flask import Flask, render_template
from models import storage, State, Amenity 


app = Flask(__name__)


@app.teardown_appcontext
def close_session(cls):
    """Closes session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def states_state(id=None):
    """displays a HTML page like 6-index.html"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', **locals())


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
