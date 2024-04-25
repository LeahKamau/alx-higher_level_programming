#!/usr/bin/python3
"""This module contains class Base"""


class Base:
    """Base class for managing the id attribute in all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor

        Args:
            id (int, optional)
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id =  Base.__nb_objects
