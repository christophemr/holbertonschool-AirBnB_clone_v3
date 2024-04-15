#!usr/bin/python3
"""
creat a Flask app and register the blueprint app_views
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def close_db(obj):
    """ calls methods close() """
    storage.close()


if __name__ == '__main__':

    HOST = getenv('HBNB_API_HOST', default='0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', default=5000))

    app.run(host=HOST, port=PORT, threaded=True)
