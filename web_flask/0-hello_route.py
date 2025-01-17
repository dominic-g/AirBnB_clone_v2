#!/usr/bin/python3
"""This script starts a Flask web application"""


from flask import Flask
import subprocess


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """This function executes when the 0.0.0.0:5000/ is requested"""
    return 'Hello HBNB!'


@app.route('/airbnb-onepage', strict_slashes=False)
def hello_world_2():
    """This function executes when the 0.0.0.0:5000/airbnb-onepage is requested"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    subprocess.run("export", "FLASK_APP=0-hello_route.py")
    subprocess.run("flask run")
