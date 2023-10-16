#!/usr/bin/python3
"""make city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class

    Attributes:
        state_id (str): the state id
        name (str): the name
    """

    state_id = ""
    name = ""
