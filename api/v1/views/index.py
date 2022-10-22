#!/usr/bin/python3

from api.v1.views import app_views

statuss = {
    "status": "OK"
}


@app_views.route('/status', strict_slashes=False)
def status():
    """Return the status of the server"""
    return statuss
