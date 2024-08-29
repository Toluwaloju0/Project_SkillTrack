#!/usr/bin/python3
""" The badge module"""

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class Badge(BaseModel, Base):
    """The badge table"""
    __tablename__ = 'badges'

    name = Column(String(60), nullable=False, unique=True)

    # relationship
    users = relationship('User', back_populates='badge')
