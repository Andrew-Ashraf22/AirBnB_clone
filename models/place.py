#!/usr/bin/python3
"""make place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """place class

    Attributes:
        city_id (str): the city id
        user_id (str): the user id
        name (str): the name
        description (str): the description
        number_rooms (int): the number of rooms
        number_bathrooms (int): the number of bathrooms
        max_guest (int): the maximum number of guests
        price_by_night (int): the price by night
        latitude (float): the latitude
        longitude (float): the longitude
        amenity_ids (list):list of amenity ids
    """

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
