#!/usr/bin/python3
"""
    Create flask application instance (app)
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
        Response to request main URL "/" or not in @app.route()
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
