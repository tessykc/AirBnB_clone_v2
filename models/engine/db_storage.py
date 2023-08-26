#!/usr/bin/python3
"""
DBStorage module for HBNB project
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base


class DBStorage:
    """
    This class manages storage of hbnb models using SQLAlchemy
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize DBStorage instance
        """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session 
        all objects depending on class name
        """
        from models import classes
        result = {}
        if cls:
            for key, value in self.__session.query(classes[cls]).all():
                result[key] = value
        else:
            for key, value in classes.items():
                if value.__name__ != 'BaseModel':
                    for obj in self.__session.query(value).all():
                        key = "{}.{}".format(obj.__class__.__name__, obj.id)
                        result[key] = obj
        return result

    def new(self, obj):
        """
        Add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and 
        create the current database session
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
