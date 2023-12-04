#!/usr/bin/python3


"""Defines the BaseModel class."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of HBnB project."""

    def __init__(self):
        """Initialize a new BaseModel."""

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """Update updated_at with the current datetime"""

        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary of the BaseModel instance.
        Including the key/value pair __class__ representing
        the class name of the object.
        """

        rtndict = self.__dict__.copy()
        rtndict["created_at"] = self.created_at.isoformat()
        rtndict["updated_at"] = self.updated_at.isoformat()
        rtndict["__class__"] = self.__class__.__name__
        return rtndict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""

        clname = self.__class__.__name__
        return ("[{}] ({}) {}".format(clname, self.id, self.__dict__))
