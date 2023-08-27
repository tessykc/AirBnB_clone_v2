#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id')),
                      Column('amenity_id', String(60), ForeignKey('amenities.id')))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            review_list = []
            for obj in models.storage.all(Review).items():
                if obj.place_id == self.id:
                    review_list.append(obj)
            return review_list

        @property
        def amenities(self):
            my_list = []
            for obj in models.storage.all(Amenity):
                if obj.id in self.amenity_ids:
                    my_list.append(obj)
            return my_list

        @amenities.setter
        def amenities(self, obj=None):
            if obj is not None and type(obj) is Amenity:
                self.amenity_ids.append(obj.id)

    def add_amenity(self, amenity):
        """Add an Amenity to the place's amenities"""
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
