#!/usr/bin/python3
"""Module that contains save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation
    """

    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
