#!/usr/bin/python3
"""A module to test the classes"""

from models.base_model import BaseModel, Base
from models.skill import Skill
from models.badge import Badge
from models.user import User
from models.resource import Resource
from models.progress import Progress


skill_1 = Skill(name="Fishing")
print(skill_1.id)
print(skill_1.__dict__)

badge_1  = Badge(name='Badge 1')
print(badge_1.id)
print("Badge 1 - {}".format(badge_1.__dict__))

skill_1.resources = [Resource(name='for_fishing'), Resource(name='for_fishing')]
