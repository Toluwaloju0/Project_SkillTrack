#!/usr/bin/python3
"""The resources table for each skill"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Resource(BaseModel, Base):
    """The resources table"""
    __tablename__ = 'resources'

    name = Column(String(100), nullable=False)
    skill_id = Column(String(60), ForeignKey('skills.id'))

    # relationship
    skill = relationship('Skill', back_populates='resources')
