#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel):
    """ Amenity class """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place",secondary="place_amenity")

    def places(self):
        """Getter attribute for places using FileStorage"""
        places_list = []
        all_places = models.storage.all(Place)
        for place in all_places.values():
            if self.id in place.amenity_ids:
                places_list.append(place)
        return places_list
