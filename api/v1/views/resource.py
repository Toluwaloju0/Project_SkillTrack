#!/usr/bin/python3
"""A module to define the resource api"""


from api.v1.views import Api_skill
from flask import jsonify, abort
from models import storage
from models.resource import Resource


@Api_skill.route('/skills/<skill_id>/resources', strict_slashes=False)
def get_skill_resource(skill_id):
    """To get all resources on a particular skill"""

    from models.skill import Skill

    skill = storage.get_user(Skill, skill_id)
    if not skill:
        abort(404)
    r_list = []
    for resource in skill.resources:
        r_list.append(resource.to_dict())
    return jsonify(r_list)


@Api_skill.route('/resources', strict_slashes=False)
@Api_skill.route('/resources/<resource_id>')
def get_resource(resource_id=None):
    """To get a resource instance or all resource instances"""

    if resource_id:
        resource = storage.get_user(Resource, id=resource_id)
        if not resource:
            abort(404)
        return jsonify(resource.to_dict())
    else:
        r_list = []
        resources = storage.all(Resource)
        for key in resources.keys():
            r_list.append(resources[key].to_dict())
        return jsonify(r_list)


@Api_skill.route('/resources/<resource_id>', methods=['DELETE'])
def del_resource(resource_id):
    """To delete a resource"""

    resource = storage.get_user(Resource, id=resource_id)
    if not resource:
        abort(404)
    resource.delete()
    return jsonify({})


@Api_skill.route('/skills/<skill_id>/resources', methods=['POST'])
def create_resource(skill_id):
    """To create a new resource for a skill"""

    from flask import request
    from models.skill import Skill

    # Get the request and data
    if not request.is_json:
        abort(400, description='Add the Content-Type header')
    data = request.get_json()
    if not data.get('name'):
        abort(400, description='name not included')
    # Get the skill
    skill = storage.get_user(Skill, id=skill_id)
    if not skill:
        abort(404)
    skill.resources.append(Resource(**data))
    resource = skill.resources[-1]
    skill.save()
    return jsonify(resource.to_dict())


@Api_skill.route('/resources/<resource_id>', methods=['PUT'])
def update_resource(resource_id):
    """To updata a resource instance"""

    from flask import request

    # Get the request and data
    if not request.is_json:
        abort(400, description='Please include the Content-Type header')
    data = request.get_json()
    if data.get('skill_id'):
        abort(400, description='The skill cant be changed!!!')
    # Get the resource instance
    resource = storage.get_user(Resource, id=resource_id)
    if not resource:
        abort(404)
    for key, value in data.items():
        setattr(resource, key, value)
    resource.save()
    return jsonify(resource.to_dict())
