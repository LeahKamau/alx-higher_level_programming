#!/usr/bin/python3
"""This module comprises of lookup function"""

def lookup(obj):
    """
    This function that returns the list of available attributes and methods of an object

    Args:
        obj: parameter passed

    Returns:
        list of available attributes and methods of an object
    """

    return dir(obj)
