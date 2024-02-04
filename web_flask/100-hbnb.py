#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/hbnb')
def hbnb():
    """
    Display a HTML page like 8-index.html.
    """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()

    states = sorted(states, key=lambda x: x.name)
    cities = sorted(cities, key=lambda x: x.name)
    amenities = sorted(amenities, key=lambda x: x.name)
    places = sorted(places, key=lambda x: x.name)

    return render_template(
        '100-hbnb.html',
        states=states,
        cities=cities,
        amenities=amenities,
        places=places
    )

@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
