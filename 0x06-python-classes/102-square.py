#!/usr/bin/python3
"""Class Square that defines a square object"""


class Square:
    """Class Square that defines a square object"""

    def __eq__(self, other):
        return self.__size == other.__size

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

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

    def area(self):
        """Method that returns the current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieves size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to value

        Args:
            value (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
