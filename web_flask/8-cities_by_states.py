#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template

# Create a Flask constructor.
# It takes name of the current module as the argument
app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext_handle(error):
    """" remove the current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_cities():
    """
    Method to render all cities
    """
    states = {}
    state_dictionary = storage.all(State)
    for key, value in sorted(state_dictionary.items()):
        states[value.id] = value
    return render_template('8-cities_by_states.html', states=states)


# Create the main driver function
if __name__ == '__main__':
    # call the run method
    app.run(host="0.0.0.0", port="5000")
