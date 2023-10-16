#!/usr/bin/python3
"""make state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """state class

    Attributes:
        name (str): the name
    """

    name = ""
