#!/usr/bin/python3
"""This is the index"""

from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from api.v1.views import app_views
from flask import jsonify


classes = {"users": "User", "places": "Place", "states": "State",
           "cities": "City", "amenities": "Amenity",
           "reviews": "Review"}


@app_views.route('/status', methods=['GET'])
def status():
    """ Takes you to the sttau spage"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
def count():
    """Retirves the number of each objects by thier type"""
    count_dict = {}
    for cls in classes:
        count_dict[cls] = storage.count(classes[cls])
    return jsonify(count_dict)
