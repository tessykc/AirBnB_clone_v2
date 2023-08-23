#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    # name = ""
    __tablename__ = 'states'
    name = Column(String (128), nullable=False) 
    cities = relationship('City', backref='state', cascade='all, delete-orphan')
