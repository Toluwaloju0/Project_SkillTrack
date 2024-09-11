#!/usr/bin/python3
"""The storage engine for the database"""

from sqlalchemy import create_engine


class DBStorage:
    """The class to store the information to a database"""

    __session = None
    __engine = None

    def __init__(self, user="", pwd="", db=""):
        """The initialisation function"""

        DBStorage.__engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@localhost/{db}",
            pool_pre_ping=True)
        self.classes = []

    def reload(self):
        """To get all instances to a database"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.badge import Badge
        from models.skill import Skill
        from models.progress import Progress
        from models.resource import Resource
        from sqlalchemy.orm import scoped_session, sessionmaker
        self.classes = [User, Badge, Skill, Resource, Progress]

        # create and map all tables
        Base.metadata.create_all(DBStorage.__engine)
        # create a session to query the table
        Session = scoped_session(sessionmaker(
                bind=DBStorage.__engine,
                expire_on_commit=False)
            )
        DBStorage.__session = Session()

    def new(self, obj):
        """To add the instance of a class to the database"""
        DBStorage.__session.add(obj)
        self.save()

    def save(self):
        """To save all changes to the database"""
        DBStorage.__session.commit()

    def delete(self, obj):
        """To delete an obj in the database"""
        DBStorage.__session.delete(obj)
        self.save()

    def all(self, cls=None):
        """To get all information in the database"""
        cls_dict = {}
        # if class query the class
        if cls:
            objects = DBStorage.__session.query(cls).all()
            for obj in objects:
                key = cls.__name__ + '.' + obj.id
                cls_dict[key] = obj

        else:
            for cls in self.classes:
                objects = DBStorage.__session.query(cls).all()
                for obj in objects:
                    key = cls.__name__ + '.' + obj.id
                    cls_dict[key] = obj
        return cls_dict

    def get_user(self, cls, id=None):
        """To get a user in the database"""
        if not id:
            return None
        return DBStorage.__session.query(cls).filter(cls.id==id).one_or_none()
