#!/usr/bin/python3
"""Index page of the domain"""

from models import storage
from api.v1.views import app_views

statuss = {
    "status": "OK"
}


@app_views.route('/status', strict_slashes=False)
def status():
    """Return the status of the server"""
    return statuss


@app_views.route('/stats', strict_slashes=False)
def statistics():
    """Return the statistics of the objects"""
    statist = {
        "amenities": storage.count('Amenity'),
        "cities": storage.count('City'),
        "places": storage.count('Place'),
        "reviews": storage.count('Review'),
        "states": storage.count('State'),
        "users": storage.count('User')
    }

    return statist
