#!/usr/bin/python3
"""View to handle all Users objects"""

from models import storage
from api.v1.views import app_views
from models.base_model import BaseModel
from flask import jsonify, abort, request, make_response
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def all_users():
    """Return all users objects"""
    users = storage.all(User)
    userss = []
    for user in users.values():
        userss.append(user.to_dict())
    return jsonify(userss)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def one_user(user_id):
    """Get a single user object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_user(user_id):
    """Delete a user obj with its id"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    user.delete()
    storage.save()
    return make_response({}, 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """Post new user object"""
    post_req = request.get_json()
    if not post_req:
        abort(400, "Not a JSON")
    if 'email' not in post_req:
        abort(400, "Missing email")
    if 'password' not in post_req:
        abort(400, "Missing password")

    new_user = User(**post_req)
    storage.new(new_user)
    storage.save()
    return make_response(new_user.to_dict(), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """Update the user object with the provided id"""
    put_req = request.get_json()
    if not put_req:
        abort(400, "Not a JSON")
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    ignore_keys = ['id', 'created_id', 'updated_at', 'email']

    for key, value in put_req.items():
        if key not in ignore_keys:
            setattr(user, key, value)
    storage.save()
    return make_response(user.to_dict(), 200)
