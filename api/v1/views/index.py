#!/usr/bin/python3

from api.v1.views import app_views

status = {
    "status": "OK"
}


@app_views.route('/status')
def status():
    """Return the status of the server"""
    return status
