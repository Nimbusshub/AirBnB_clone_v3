#!/usr/bin/python3

from api.v1.views import app_views
from flask import Flask

status = {
    "status": "OK"
}


@app_views.route('/status')
def return_status():
    return status
