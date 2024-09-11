#!/usr/bin/python3
"""A module to create the badge api"""

from api.v1.views import Api_skill
from flask import jsonify, abort
from models import storage
from models.badge import Badge


@Api_skill.route('/badges', strict_slashes=False)
@Api_skill.route('/badges/<badge_id>')
def get_badge(badge_id=None):
    """To get a badge instance of all badges available"""

    if badge_id:
        badge = storage.get_user(Badge, badge_id)
        if not badge:
            abort(404)
        return jsonify(badge.to_dict())
    b_list = []
    badges = storage.all(Badge)
    for key in badges.keys():
        b_list.append(badges[key].to_dict())
    return jsonify(b_list)


@Api_skill.route('/badges/<badge_id>', methods=['DELETE'])
def del_badge(badge_id):
    """To delete a badge instance"""

    badge = storage.get_user(Badge, id=badge_id)
    if not badge:
        abort(404)
    badge.delete()
    return({})


@Api_skill.route('/badges', methods=['POST'], strict_slashes=False)
def create_badge():
    """To create a new badge inctance"""

    from flask import request
    
    # Get the request and data
    if not request.is_json:
        abort(400, description='Please add the Content-Type header')
    data = request.get_json()
    if not data.get('name'):
        abort(400, description='Name is missing in request')
    # Create the Instance
    badge = Badge(**data)
    badge.new()
    return jsonify(badge.to_dict())


@Api_skill.route('/badges/<badge_id>', methods=['PUT'])
def update_badge(badge_id):
    """To update a badge instance"""

    from flask import request

    # Get the request and data
    if not request.is_json:
        abort(400, description='Please add the Content-Type header')
    data = request.get_json()
    # Get the badge instance
    badge = storage.get_user(Badge, badge_id)
    if not badge:
        abort(404)
    for key, value in data.items():
        setattr(badge, key, value)
    badge.save()
    return jsonify(badge.to_dict())
