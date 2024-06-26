#!/usr/bin/python3
"""This module comprises from_json_string function"""
import json


def from_json_string(my_str):
    """function that returns an object represented by a JSON string

    Args:
        my_str: json string to object"""

    return json.loads(my_str)
