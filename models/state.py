#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    name = ""
    __tablename__ = 'states'
    name = Column(String (128), nullable=False)
    for DBStorage:
        cities = relationship('City', cascade = 'all, delete', backref = 'state')
    for FileStorage:
        getattr cities()
        return (City)
    City.state_id = State.id
    FileStorage = relationship('State', 'City')
