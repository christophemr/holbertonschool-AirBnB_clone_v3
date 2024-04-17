#!/usr/bin/python3
"""
This module contains the principal application
"""
from models import storage
from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from os import getenv
from flask_cors import CORS


app = Flask(__name__)


app.register_blueprint(app_views)


CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_db(exception):
    """ Calls methods close() """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ Loads a custom 404 page not found """
    response = {"error": "Not found"}
    return jsonify(response), 404


if __name__ == "__main__":
    API_HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    API_PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=API_HOST, port=API_PORT, threaded=True)
