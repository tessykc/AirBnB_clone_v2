#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session after each request."""
    storage.close()

@app.route('/state_list', strict_slashes=False)
def state_list():
    """Display a HTML page with a list of all State objects."""
    states =storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template('states_list.html', states=sorted_states)

if __name__ == " __main__":
    app.run(host='0.0.0.0', port=5000)
