#!/usr/bin/python3
"""make review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class

    Attributes:
        place_id (str): the place id
        user_id (str): the user id
        text (str): the text
    """

    place_id = ""
    user_id = ""
    text = ""
