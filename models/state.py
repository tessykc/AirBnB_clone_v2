#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
import os
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    #cities = relationship('City', cascade='all, delete', backref='state')
    if os.getenv("HBNB_TYPE_STORAGE") != "db": 
        @property
        def cities(self):
            """Returns the list of City instances with state_id equals to the current State.id"""
            city_list = []
            city_dict = models.storage.all(models.city.City)
            for key, value in city_dict.items():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

    else:
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
