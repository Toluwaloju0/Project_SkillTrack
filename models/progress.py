#!/usr/bin/python3
"""The user progress table"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Progress(BaseModel, Base):
    """The progress table"""
    __tablename__ = 'progress'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    score = Column(Float, nullable=False, default=0.0)

    # relationship
    user_progress = relationship('User', back_populates='progress')
