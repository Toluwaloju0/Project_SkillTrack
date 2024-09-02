"""The model init file"""

from models.engine.db_storage import DBStorage

storage = DBStorage(user="Tolu_skill", pwd="Toluwaloju2002", db="skill_test")
storage.reload()
