#!/usr/bin/python3
"""Class that defines value and method that raises exception"""


class BaseGeometry:
    """class that defines value and method that raises exception"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks value is an int and not less or equal to 0

        Args:
            name: name of the instance
            value: value of instance attribute

        Raises:
            TypeError: if value is not int
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
