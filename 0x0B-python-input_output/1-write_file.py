#!/usr/bin/python3
"""This module comprises of write_file function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file

    Args:
        filename: file to write to
        text: text to write to filename

    Return: the number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
