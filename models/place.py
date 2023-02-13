#!/usr/bin/env python3
"""class inheriting from BaseModel"""

from models.base_model import BaseModel


class Place(BaseModel):
    """class with city id, user id, name, description, number_rooms,"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    lattitude = 0.0
    longitude = 0.0
    amenity_id = []