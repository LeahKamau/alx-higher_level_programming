#!/usr/bin/python3
"""Class Square that defines a square object"""


class Square:
    """Class Square that defines a square object"""

    def __init__(self, size=0):
        """Initializes a new square with default value 0

        Args:
            size (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
