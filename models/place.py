#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from os import environ as env

metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('places.id'), primary_key=True)
                     
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    def amenities(self):
        """ relationship with the class Amenity """
        if env.get('HBNB_TYPE_STORAGE') == 'db':
            amenities = relationshiprelationship("Amenity",
                    secondary=place_amenity, viewonly=False)

        """ getting amenities within the place id """
        ls = [
            v for k, v in model.storage.all(model.Amenity).items()
              if v.id in self.amenity_ids]
        
        return (ls)
        for amenities in amenity_ids:
            result.append(Amenity.id)
        return result
