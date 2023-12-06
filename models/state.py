#!/usr/bin/python3

"""Defines a class State. """

from models.vase_model import BaseModel


class State(BaseModel):
    """ Class place that inherits from BaseModel
        Public class attributes:
            name: (str) - Name of the state
    """

    name = ""

