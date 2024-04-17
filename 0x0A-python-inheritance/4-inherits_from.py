#!/usr/bin/python3
"""This module comprises of inherits_from function"""


def inherits_from(obj, a_class):
    """ Function returns True if obj is an instance of a_class that inherited
    directly or indirectly from the specified class; otherwise False

    Args:
        obj: object to check
        a_class: specified class
    """

    if type(obj) is a_class:
        return False
    if isinstance(obj, a_class):
        return True
