#!/usr/bin/python3
"""
    Create flask application instance (app)
"""
from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def remove_session():
    """
        after each request : remove current SQLAlchemy Session
    """
    storage.close()

@app.route("/states_list", strict_slashes=False)
def list_states():
    """
        Display a HTML page:
        h1 tag "States"
        UL tag list of all State objects present in DBStorage
            sorted by name(A->Z)
            LI tag : description of one State:<state.id>: <B><state.name></B>
    """
    states = storage.all()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
