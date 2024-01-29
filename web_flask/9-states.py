#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the storage on teardown."""
    storage.close()

@app.route('/states', strict_slashes=False)
def list_states():
    """Display a list of all states."""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def show_state(id):
    """Display information about a specific state."""
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('state.html', state=state, cities=cities)
    else:
        return render_template('not_found.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
                                                                                
