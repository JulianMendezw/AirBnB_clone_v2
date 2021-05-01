#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template

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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_user_text_2(text):
    """ Take a argument and return it """
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def show_user_number(n):
    """Show a number if the argument is a number """
    return ("%d is a number" % n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', value=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """ even or odd number"""
    string = "is even" if n % 2 == 0 else "is odd"
    return render_template('6-number_odd_or_even.html', n=n, string=string)


# Create the main driver function
if __name__ == '__main__':
    # call the run method
    app.run(host="0.0.0.0", port="5000")