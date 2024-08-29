#!/usr/bin/python3
"""This is the BaseModel class"""

from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()


class BaseModel:
    """The BaseModel class"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """To initialize the class"""

        self.id = str(uuid4())
