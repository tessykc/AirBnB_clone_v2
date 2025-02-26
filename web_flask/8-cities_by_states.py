#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False
@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request."""
    storage.close()
@app.route('/cities_by_states')
def cities_by_states():
    """display a HTML page"""
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda x: x.name)
    return render_template('cities_by_states.html', states=states_sorted)




if __name__ == " __main__":
        app.run(host='0.0.0.0', port=5000)
