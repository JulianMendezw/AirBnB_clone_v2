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
def cities_list():
    """ displays a HTML page with a list of cities by states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])
    return render_template('8-cities_by_states.html',
                           states=st_ct,
                           h_1="States")


# Create the main driver function
if __name__ == '__main__':
    # call the run method
    app.run(host="0.0.0.0", port="5000")
