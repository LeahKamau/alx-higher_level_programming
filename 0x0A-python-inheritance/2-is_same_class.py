#!/usr/bin/python3
"""This module comprises of is_same_class"""


def is_same_class(obj, a_class):
    """ function returns True if object is exactly an instance of specified class
    otherwise False

    Args:
        obj: object to check
        a_class: specified class
    """

    if type(obj) is a_class:
        return True
    return False
