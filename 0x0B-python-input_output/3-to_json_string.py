#!/usr/bin/python3
"""This module comprises to_json_string function"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)

    Args:
        my_obj: object to convert to json representataion"""

    return json.dumps(my_obj)
