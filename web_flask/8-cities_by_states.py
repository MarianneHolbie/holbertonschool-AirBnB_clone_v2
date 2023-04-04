#!/usr/bin/python3
"""
    Create flask application instance (app)
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_byStates():
    """
        Display a HTML page:
        h1 tag "States"
        UL tag list of all State objects present in DBStorage
            sorted by name(A->Z)
            LI tag : description of one State:<state.id>: <B><state.name></B>
                ul tag: list of City linked sorted by name(A->Z)
                LI tag: description <city.id>: <B><city.name></B>
    """
    bd = storage.all(State)
    city_states = []
    for v in bd.values():
        city_states.append(v)
    return render_template('8-cities_by_states.html', states=city_states)


@app.teardown_appcontext
def remove_session(exception):
    """
        after each request : remove current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
