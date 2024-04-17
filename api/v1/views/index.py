#!usr/bin/python3
"""
Create a Flask app; app_views
"""
from flask import jsonify
from flask import Flask
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def api_status():
    """
    Retrieves the status of the API.
    Returns:
        JSON response indicating the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_object_counts():
    """
    Retrieves the number of each object by type.
    Returns:
        JSON response with counts for different object types
    """
    counts = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(counts)
