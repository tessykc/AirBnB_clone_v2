#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Teardown app context"""
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display HBNB filters HTML page"""
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()
    return render_template(
    '10-hbnb_filters.html',
    states=sorted(states, key=lambda x: x.name),
    cities=sorted(cities, key=lambda x: x.name),
    amenities=sorted(amenities, key=lambda x: x.name)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

