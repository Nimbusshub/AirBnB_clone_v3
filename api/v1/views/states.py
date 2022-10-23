#!/usr/bin/python3
"""View to handle all state objects"""

from models import storage
from api.v1.views import app_views
from models.base_model import BaseModel
from flask import jsonify, abort, request, make_response
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():
    """Return all states objects"""
    states = storage.all('State')
    statess = []
    for state in states.values():
        statess.append(state.to_dict())
    return jsonify(statess)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def one_state(state_id):
    """Get a single state"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def del_state(state_id):
    """Delete a state obj with its id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    state.delete()
    storage.save()
    return make_response({}, 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """Post new state object"""
    try:
        post_req = request.get_json()
    except Exception:
        abort(400, "Not a JSON")
    if 'name' not in post_req:
        abort(400, "Missing name")

    new_state = State(**post_req)
    storage.new(new_state)
    storage.save()
    return make_response(new_state.to_dict(), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """Update the state object with the provided id"""
    try:
        post_req = request.get_json()
    except Exception:
        abort(400, "Not a JSON")

    state = storage.get(State, state_id)
    if not state:
        abort(404)
    ignore_keys = ['id', 'created_id', 'updated_at']

    for key, value in post_req.items():
        if key not in ignore_keys:
            setattr(state, key, value)
    storage.save()
    return make_response(state.to_dict(), 200)
