#!/usr/bin/python3
"""make a base class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """the basemodel class"""

    def __init__(self, *args, **kwargs):
        """make a new basebodel

        Args:
            *args (any): not used
            **kwargs (dict): dict of args for the class
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, tform)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """update the update_at var"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """return a dict reps of basemodel"""
        dicti = self.__dict__.copy()
        dicti["created_at"] = self.created_at.isoformat()
        dicti["updated_at"] = self.updated_at.isoformat()
        dicti["__class__"] = self.__class__.__name__
        return dicti

    def __str__(self):
        """return the string reps of basemodel"""
        n = self.__class__.__name__
        return "[{}] ({}) {}".format(n, self.id, self.__dict__)
