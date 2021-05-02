#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from flask import Flask, render_template

# Create a Flask constructor.
# It takes name of the current module as the argument
app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext_handle(error):
    """" remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ displays a HTML page with a list of states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)


# Create the main driver function
if __name__ == '__main__':
    # call the run method
    app.run(host="0.0.0.0", port="5000")
