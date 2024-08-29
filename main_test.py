#!/usr/bin/python3
"""A module to test the classes"""

from models.base_model import BaseModel, Base
from models.skill import Skill
from models.badge import Badge
from models.user import User
from models.resource import Resource
from models.progress import Progress


skill_1 = Skill(name="Fishing")
print(skill_1.__dict__)

badge_1  = Badge()
print("Badge 1 - {}".format(badge_1.__dict__))

