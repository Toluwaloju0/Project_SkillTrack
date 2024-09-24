#!/usr/bin/python3
"""The state api module"""


from api.v1.views import Api_skill
from flask import jsonify, abort
from models.skill import Skill
from models import storage


@Api_skill.route('/skills', strict_slashes=False)
@Api_skill.route('/skills/<skill_id>')
def get_states(skill_id=None):
    """To get a skill instance or all skills instances"""

    if skill_id:
        skill = storage.get_user(Skill, id=skill_id)
        if not skill:
            abort(404)
        return jsonify(skill.to_dict())
    else:
        s_list = []
        skills = storage.all(Skill)
        for key in skills.keys():
            s_list.append(skills[key].to_dict())
        return jsonify(s_list)


@Api_skill.route('/skills/<skill_id>', methods=['DELETE'])
def delete(skill_id):
    """To delete an instance"""

    skill = storage.get_user(Skill, id=skill_id)
    if not skill:
        abort(404)
    skill.delete()
    return jsonify({})


@Api_skill.route('/skills', methods=['POST'], strict_slashes=False)
def create_skill():
    """To create a new skill instance"""

    from flask import request

    # Get the request header
    if not request.is_json:
        abort(400, description='Please include Content-type: application/json')
    data = request.get_json()
    if not data.get('name'):
        abort(400, description='No Skill name given')
    # Create the new skill
    skill = Skill(**data)
    skill.new()
    return jsonify(skill.to_dict())


@Api_skill.route('/skills/<skill_id>', methods=['PUT'])
def update_skill(skill_id):
    """To update a skill instance"""

    from flask import request

    # Get the skill instance
    skill = storage.get_user(Skill, id=skill_id)
    if not skill:
        abort(404)
    # Get the  request and data
    if not request.is_json:
        abort(400, description='Please add Content-Type header')
    data = request.get_json()
    for key, value in data.items():
        setattr(skill, key, value)
    skill.save()
    return jsonify(skill.to_dict())
