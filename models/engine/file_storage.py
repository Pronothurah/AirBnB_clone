#!/usr/bin/env python3

""" Class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage:
    """ Class FileStorage that serilizes
    and deserialize instances to JSON
        __file_path: the path of the json file
        __objects: a dictionnary of all objects"
    """
    CLASS_MAP = {
        'BaseModel': BaseModel,
        'User': User,
        'Amenity': Amenity,
        'City': City,
        'State': State,
        'Review': Review
    }

    def __init__(self):
        """ initializes FileStorage
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns a dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
            dicttionary: an empty dictionnary
                Open the dictionary in write mode
                dump the dictionary in the file f
        """
        dictionary = {}
        with open(self.__file_path, 'w') as f:
            for obj in self.__objects.values():
                key = obj.__class__.__name__ + "." + obj.id
                dictionary[key] = obj.to_dict()
            json.dump(dictionary, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
            Open in read mode"
            load the file f and read it
            """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = f.read()
                if data:
                    my_dict = json.loads(data)
                    self.__objects.clear()
                    for key, value in my_dict.items():
                        class_name, obj_id = key.split('.')
                        if class_name in self.CLASS_MAP:
                            obj_class = self.CLASS_MAP[class_name]
                            instance = obj_class(**value)
                            self.new(instance)

        except FileNotFoundError:
            pass
