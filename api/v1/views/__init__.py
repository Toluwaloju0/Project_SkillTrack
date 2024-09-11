#!/usr/bin/python3
"""The init package to create a blueprint"""

from flask import Blueprint

Api_skill = Blueprint('Api_skill', __name__, url_prefix='/api/v1')

from api.v1.views.user import *
from api.v1.views.skill import *
from api.v1.views.resource import *
from api.v1.views.badge import *
from api.v1.views.progress import *
