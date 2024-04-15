#!usr/bin/python3
"""
creat a Flask app; app_views
"""
from flask import jsonify
from flask import Flask
from api.v1.views import app_views


@app_views.route('/status')
def api_status():
    """
    Retrieves the status of the API.
    Returns:
        JSON response indicating the status of the API
    """
    return jsonify({"status": "OK"})
