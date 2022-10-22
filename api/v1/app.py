#!/usr/bin/python3
"""The root of my domain"""

from flask import Flask
from flask import Blueprint, render_template
from models import storage
from api.v1.views import app_views
from flask import teardown_appcontext

app = Flask(__name__)

@app.teardown_appcontext
@app.teardown_
