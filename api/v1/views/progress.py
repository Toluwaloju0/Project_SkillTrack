#!/usr/bin/python3
"""A module to create the progress api"""


from api.v1.views import Api_skill
from flask import abort, jsonify
from models import storage
from models.progress import Progress


@Api_skill.route('/users/<user_id>/progress', strict_slashes=False)
def get_user_progress(user_id):
    """To get the progress of a user"""

    from models.user import User

    # Get the user
    user = storage.get_user(User, id=user_id)
    if not user:
        abort(404)
    progress = user.progress
    if not progress:
        abort(400, description='No progress yet')
    return jsonify(progress.to_dict())


@Api_skill.route('/progress', strict_slashes=False)
@Api_skill.route('/progress/<progress_id>')
def get_progress(progress_id=None):
    """To get a progress instance or all progress instance"""

    if progress_id:
        progress = storage.get_user(Progress, id=progress_id)
        if not progress:
            abort(404)
        return jsonify(progress.to_dict())
    p_list = []
    p_dict = storage.all(Progress)
    for key in p_dict.keys():
        p_list.append(p_dict[key].to_dict())
    return jsonify(p_list)


@Api_skill.route('/progress/<progress_id>', methods=['DELETE'])
def del_progress(progress_id):
    """To delete a progress"""

    progress = storage.get_user(Progress, id=progress_id)
    if not progress:
        abort(404)
    progress.delete()
    return jsonify({})


@Api_skill.route(
    '/users/<user_id>/progress', methods=['POST'],
    strict_slashes=False)
def create_progress(user_id):
    """To create a new progress instance"""

    from models.user import User

    # Get the user and add progress
    user = storage.get_user(User, id=user_id)
    if not user:
        abort(404)
    user.progress = Progress()
    user.save()
    return jsonify(user.progress.to_dict())


@Api_skill.route('/progress/<progress_id>', methods=['PUT'])
def update_progress(progress_id):
    """To update a progress instance"""

    from flask import request

    # Get the data and request
    if not request.is_json:
        abort(404, description='Please add the Content-Type header')
    data = request.get_json()
    if not data.get('score'):
        abort(400, description='No score included')
    # Get and updata the instance
    progress = storage.get_user(Progress, id=progress_id)
    if not progress:
        abort(404)
    for key, value in data.items():
        setattr(progress, key, value)
    progress.save()

    return jsonify(progress.to_dict())
