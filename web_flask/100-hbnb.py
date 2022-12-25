#!/usr/bin/python3
"""Module: Starts a Flask web app and fetches data from storage engine"""
from flask import Flask, render_template
from models import storage, State, Amenity, Place


app = Flask(__name__)


@app.teardown_appcontext
def close_session(cls):
    """Closes session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb(id=None):
    """displays a HTML page like 8-index.html on /hbnb"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('100-hbnb.html', **locals())


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
