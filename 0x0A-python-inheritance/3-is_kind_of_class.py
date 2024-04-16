#!/usr/bin/python3
"""This module comprises of is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """ Function that returns True/False if obj is a type of a_class
    or obj is an instance of a class that inherited from, a_class

    Args:
        obj: object to check
        a_class: specified class
    """

    if isinstance(obj, a_class):
        return True
    return False
