#!/usr/bin/python3
"""This is the BaseModel class"""

from datetime import datetime
from models import storage
from models.engine.db_storage import DBStorage
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()


class BaseModel:
    """The BaseModel class"""
    id = Column(String(36), primary_key=True, unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # store the new instance
        self.new()

    def new(self):
        """To add a new class to the database"""
        # Add the class to the database
        storage.new(self)

    def save(self):
        """To save the class"""
        storage.save()
