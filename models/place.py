#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.user import User
from models.engine.file_storage import FileStorage
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False)
        number_bathrooms = Column(Integer, nullable=False)
        max_guest = Column(Integer, nullable=False)
        price_by_night = Column(Integer, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

<<<<<<< HEAD
        reviews = relationship('Review', backref='place', cascade='delete')

        place_amenity = Table('place_amenity',
                              Base.metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'),
                                     primary_key=True, nullable=False),
                              Column('amenity_id',
                                     String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True, nullable=False))
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
=======
>>>>>>> e56b727aca91cf63f611ee4251da4b92296e3a93
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
