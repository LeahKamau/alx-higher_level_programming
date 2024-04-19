#!/usr/bin/python3
"""This module comprises append_write function"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file

    Args:
        filename: name of file to append
        text: text to append

    Returns: number of characters added
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
