#!/usr/bin/python3
"""make User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """the user class

    Attributes:
        email (str): the email
        password (str): the password
        first_name (str): the first name
        last_name (str): the last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
