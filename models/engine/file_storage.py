#!/usr/bin/python3
"""makes a filestorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """the filestorage class

    Attributes:
        __file_path (str): storage file
        __objects (dict): a dict of the objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """add the obj to the objects dict"""
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """Serialize __objects to the file"""
        objs = {}
        for key, o in FileStorage.__objects.items():
            objs[key] = o.to_dict()
        with open(FileStorage.__file_path, 'w') as _file:
            json.dump(objs, _file)

    def reload(self):
        """Deserialize json file"""
        try:
            with open(FileStorage.__file_path) as f:
                ddict = json.load(f)
                for k, v in ddict.items():
                    cn, iid = k.split('.')
                    obj = eval(cn)(**v)
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
            return
