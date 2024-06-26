#!/usr/bin/python3
"""This module comprises of is_same_class"""


def is_same_class(obj, a_class):
    """ Function that returns True/False if obj is a type of a_class

    Args:
        obj: object to check
        a_class: specified class
    """

    if type(obj) is a_class:
        return True
    return False
