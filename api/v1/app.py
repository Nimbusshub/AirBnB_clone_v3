#!/usr/bin/python3
"""Import Blueprint"""

from flask import Flask, make_response
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    return make_response({"error": "Not found"}, 404)


if __name__ == '__main__':
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')
    host, port = '0.0.0.0', 5000
    if HBNB_API_HOST:
        host = HBNB_API_HOST
    if HBNB_API_PORT:
        port = HBNB_API_PORT
    app.run(host=host, port=port, threaded=True)
