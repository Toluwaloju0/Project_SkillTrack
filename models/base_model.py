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
        t_format = "%Y%m%d%H%M%S%f"
        if kwargs:
            if kwargs.get('class'):
                del kwargs['class']
            for key, value in kwargs.items():
                # Check and update the id, created_at, updated_at
                if not kwargs.get('id'):
                    self.id = str(uuid4())
                if kwargs.get('created_at'):
                    self.created_at = datetime.strptime(
                        kwargs['created_at'], t_format)
                else:
                    self.created_at = datetime.now()

                if kwargs.get('updated_at'):
                    self.updated_at = datetime.strptime(
                        kwargs['updated_at'], t_format)
                else:
                    self.updated_at = datetime.now()

                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def new(self):
        """To add a new class to the database"""
        storage.new(self)

    def save(self):
        """To save the class"""

        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """To print an instance"""
        return f"{self.to_dict()}"

    def to_dict(self):
        """To convert the instance to a dictionary"""

        t_format = "%Y%m%d%H%M%S%f"
        dispose = [
            'skill', 'resources', 'user_skills', 'skills',
            'progress', 'badge', 'skill', 'user_progress', 'users']

        my_dict = {}
        my_dict.update(self.__dict__)
        if my_dict.get('_sa_instance_state'):
            del my_dict['_sa_instance_state']
        for Del in dispose:
            if my_dict.get(Del):
                del my_dict[Del]
        my_dict['class'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.strftime(t_format)
        my_dict['updated_at'] = self.updated_at.strftime(t_format)
        return my_dict

    def delete(self):
        """To delete an instance"""
        storage.delete(self)
