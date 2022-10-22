#!/usr/bin/python3
"""The root of my domain"""

from flask import Flask
from flask import Blueprint, render_template
from models import storage
from api.v1.views import app_views
from flask import teardown_appcontext

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')
    host, port = '', 0
    if HBNB_API_HOST:
        host = HBNB_API_HOST
    else:
        host = '0.0.0.0'
    if HBNB_API_PORT:
        port = HBNB_API_PORT
    else:
        port = 5000

    app.run(host=host, port=port, threaded=True)
