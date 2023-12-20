#!/usr/bin/python3
"""Class Square that defines a square object"""


class Square:
    """Class Square that defines a square object"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square with default value 0

        Args:
            size (int): size of the square
            position (tuple)
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Method that returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Method that prints in stdout the square
        with the character #"""
        if not self.__size:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

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

    @property
    def position(self):
        """Retrieves the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position to value"""
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or value[0] < 0 or
                type(value[1]) is not int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """Returns a string representation of the square"""
        output = ""

        if self.size == 0:
            output += "\n"
        else:
            for i in range(self.position[1]):
                output += "\n"
            for i in range(self.size):
                output += " " * self.position[0]
                output += "#" * self.size
                if i != self.size - 1:
                    output += "\n"
        return output
