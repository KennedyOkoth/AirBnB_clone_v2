#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Hello function
    :return: Hello HBNB
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    HBNB function
    :return: HBNB
    """
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """

    :param text:
    :return:
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
