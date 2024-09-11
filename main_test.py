#!/usr/bin/python3
"""A module to test the classes"""

from models import storage
from models.base_model import BaseModel, Base
from models.skill import Skill
from models.badge import Badge
from models.user import User
from models.resource import Resource
from models.progress import Progress
from time import sleep

skill_1 = Skill(name="Fishing")
skill_1.new()
skill_1.resources = [Resource(name='Fishing resource 00'), Resource(name='for_fishing 01')]
skill_1.save()

user_1 = User(name='John Samuel')
user_1.new()

badge_1 = Badge(name='Starter')
badge_1.new()

user_1.progress = [Progress()]
user_1.save()

all_cls = storage.all()
for key, value in all_cls.items():
    print("This is the key", key)
    print(value)
    print('---------------------------------------------')

