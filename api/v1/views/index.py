#!/usr/bin/python3
"""Index page of the domain"""

from api.v1.views import app_views
from models import storage

statuss = {
    "status": "OK"
}

@app_views.route('/status', strict_slashes=False)
def status():
    """Return the status of the server"""
    return statuss
