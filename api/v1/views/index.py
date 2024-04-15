#!usr/bin/python3
"""
creat a Flask app; app_views
"""
from models import storage
from flask import jsonify
from flask import Flask
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def api_status():
    """
    Retrieves the status of the API.
    Returns:
        JSON response indicating the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
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
