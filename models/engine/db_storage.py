#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """int meth"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                (getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'), 
                getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query the current db"""
        objects = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls:
            if cls in classes:
                query = self.__session.query(cls).all()
                for obj in query:
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    objects[key] = obj
        else:
            for cls in classess:
                query = self.__session.query(cls).all()
                for obj in query:
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """add object to current db"""
        self.__session.add(obj)

    def save(self):
        """commit all change in cur  db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from cur db"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tb in the db"""
        Base.metadata.bind = self.__engine
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scope_session(Session)
