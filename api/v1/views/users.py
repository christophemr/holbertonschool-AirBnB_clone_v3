#!/usr/bin/python3
"""
This file contains the User module
"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    """ Get all users """
    all_list = [obj.to_dict() for obj in storage.all(User).values()]
    return jsonify(all_list)


@app_views.route('/users/<string:user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user(user_id):
    """ Get user by ID """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<string:user_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_user(user_id):
    """ Delete user by ID """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({})


@app_views.route('/users/', methods=['POST'],
                 strict_slashes=False)
def create_user():
    """ Create new user """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    user_data = request.get_json()
    if 'email' not in user_data or 'password' not in user_data:
        error_response = {"error": "Missing email or password"}
        return make_response(jsonify(error_response), 400)
    user = User(**user_data)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<string:user_id>', methods=['PUT'],
                 strict_slashes=False)
def update_user(user_id):
    """ Update user by ID """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    ignore_keys = ['id', 'email', 'created_at', 'updated_at']
    for key, value in request.get_json().items():
        if key not in ignore_keys:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict())
