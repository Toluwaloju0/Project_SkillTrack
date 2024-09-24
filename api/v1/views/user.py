#!/usr/bin/python3
"""The module to define the user api"""

from api.v1.views import Api_skill
from flask import jsonify, abort
from models import storage
from models.user import User


@Api_skill.route('/users', strict_slashes=False)
@Api_skill.route('/users/<user_id>')
def get_users(user_id=None):
    """A function to get all user instance"""

    if user_id:
        user = storage.get_user(User, id=user_id)
        if not user:
            abort(404)
        return jsonify(user.to_dict())
    else:
        user_list = []
        all_user = storage.all(User)
        for key, value in all_user.items():
            user_list.append(value.to_dict())
        return jsonify(user_list)


@Api_skill.route('/skills/<skill_id>/users', strict_slashes=False)
def skills_user(skill_id=None):
    """To get the learners of a particular skill"""

    from models import Skill

    s_users = []
    # Get the skill
    skill = storage.get_user(Skill, skill_id)
    if not skill:
        abort(404)
    for user in skill.user_skill:
        s_user.append(user.to_dict())
    return jsonify(s_user)


@Api_skill.route('/users/<user_id>', methods=['DELETE'])
def del_user(user_id):
    """To delete an instance from the database"""

    user = storage.get_user(User, id=user_id)
    if not user:
        abort(404)
    user.delete()
    return jsonify({})


@Api_skill.route('/users/', methods=['POST'], strict_slashes=False)
def create_user():
    """To create a new user"""

    from flask import request

    if not request.is_json:
        abort(400, description='Please set Content-Type: application/json')
    data = request.get_json()
    if not data.get('name'):
        abort(400, description='Name of new user not present')
    user = User(**data)
    user.new()
    return jsonify(user.to_dict())


@Api_skill.route('/users/<user_id>', methods=['PUT'])
def update(user_id):
    """To update a user instance"""

    from flask import request

    if not request.is_json:
        abort(400, description='Please set Content-Type: application/json')
    data = request.get_json()

    # Get the user instance
    user = storage.get_user(User, id=user_id)
    if not user:
        abort(404)
    # Update and save the user instance
    for key in data.keys():
        setattr(user, key, data[key])
    user.save()
    return jsonify(user.to_dict())
