#!/usr/bin/python3
"""This module comprises of read_file function"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: name of file to read
    """
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data.rstrip())
