#!/usr/bin/python3
"""
    Create flask application instance (app)
    use storage engine (DBStorage or FileStorage)
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False, methods=["GET"])
def hbnb_filters(id=None):
    """
        load all cities of State to implement popover
        load all amenities to implement popover
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def close_session(exception):
    """ remove the current SQLalchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
