#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask

# Create a Flask constructor.
# It takes name of the current module as the argument
app = Flask(__name__)

# Create a route decorator to tell the application, which URL should be
# called for the #described function and define the function.


@app.route('/', strict_slashes=False)
def web_flask():
    """ Create a route decorator to tell the application, which URL should be
        called for the #described function and define the function. """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ Return HBNB text """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_user_text(text):
    """ Take a argument and return it """
    text = text.replace('_', ' ')
    return "C " + text


# Create the main driver function
if __name__ == '__main__':
    # call the run method
    app.run(host="0.0.0.0", port="5000")
