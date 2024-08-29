#!/usr/bin/python3
"""The User module"""

from models.base_model import BaseModel, Base
from models.many import user_skill
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """The user class"""
    __tablename__ = 'users'

    name = Column(String(100), nullable=False)
    skill_id = Column(String(60), ForeignKey('skills.id'), nullable=False)
    badge_id = Column(String(60), ForeignKey('badges.id'))

    # relationship
    skills = relationship(
        'Skill',
        secondary=user_skill,
        viewonly=False,
        back_populates='user_skills'
    )

    progress = relationship(
        'Progress',
        back_populates='user_progress',
        cascade="all, delete, delete-orphan")

    badge = relationship('Badge', back_populates='users')
