#!usr/bin/python3
"""
creat a Flask app; app_views
"""
from models import storage
from flask import jsonify
from flask import Flask
from api.v1.views import app_views
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


@app_views.route('/stats', methods=['GET'],strict_slashes=False)
def count():
    """
    Retrieves the number of each objects by type
    """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
