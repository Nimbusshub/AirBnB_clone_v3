#!/usr/bin/python3
"""View to handle users review"""

from models import storage
from api.v1.views import app_views
from models.base_model import BaseModel
from flask import jsonify, abort, request, make_response
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route('/places/<place_id>/reviews',
                 methods=['GET'], strict_slashes=False)
def review_place(place_id):
    """Retrieve all review objects related to a place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    review_list = []
    for rev in place.reviews:
        review_list.append(rev.to_dict())
    return jsonify(review_list)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def one_review(review_id):
    """ Retrieves a review """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """Delete a review"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    review.delete()
    storage.save()
    return make_response({}, 200)


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def post_review(place_id):
    """Create new place review"""
    post_req = request.get_json()
    if not post_req:
        abort(400, "Not a JSON")
    if "user_id" not in post_req:
        abort(400, "Missing user_id")
    if "text" not in post_req:
        abort(400, "Missing text")

    user_id = post_req['user_id']

    __user = storage.get(User, user_id)
    __place = storage.get(Place, place_id)
    if not __user or not __place:
        abort(404)

    new_review = Review(**post_req)
    setattr(new_review, 'place_id', place_id)
    storage.new(new_review)
    storage.save()
    return make_response(new_review.to_dict(), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def put_review(review_id):
    """Update a review with the provided review id"""
    put_req = request.get_json()
    if not put_req:
        abort(400, "Not a  JSON")
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    ignore_keys = ['id', 'created_id', 'updated_at', 'user_id', 'place_id']

    for key, value in put_req.items():
        if key not in ignore_keys:
            setattr(review, key, value)
    storage.save()
    return make_response(review.to_dict(), 200)
