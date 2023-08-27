#!/usr/bin/python3
"""
DBStorage module for HBNB project
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
 

    def all(self, cls=None):
        """
        Query on the current database session 
        all objects depending on class name
        """ 
        cl_name = {"State": State,
                    "City": City,
                    "User": User,
                    "Place": Place,
                    "Review": Review,
                    "Amenity": Amenity}
        obj = {}
        cls_value = [value for key, value in cl_name.items()]
        if cls:
            if type(cls) == str:
                cls = cl_name[cls]
            cls_value = [cls]
        for one_class in cls_value:
            for value in self.__session.query(one_class):
                key = str(value.__class__.__name__) + "." + str(value.id)
                obj[key] = value
        return obj

    def new(self, obj):
        """
        Add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database sessio
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
        session_factory = sessionmaker(bind=self.__engine,
                                              expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = scoped_session(Session)

    def close(self):
        """
        Remove the method on the private session attribute
        """
        self.__session.close()
