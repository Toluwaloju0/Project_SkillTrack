#!/usr/bin/python3
"""The Skills module"""

from models.base_model import BaseModel, Base
from models.many import user_skill
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Skill(BaseModel, Base):
    """The skill class"""
    __tablename__ = 'skills'

    name = Column(String(100), nullable=False, unique=True)

    # relationship
    user_skills = relationship(
        'User',
        secondary=user_skill,
        viewonly=False,
        back_populates='skills'
    )
    resources = relationship(
        'Resource',
        back_populates='skill',
        cascade="all, delete, delete-orphan")
