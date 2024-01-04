#!/usr/bin/python3
"""Class Rectangle that defines a rectangle"""


class Rectangle:
    """Class Rectangle that defines a rectanle"""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle with default
        width 0 and height 0 or passed values

        Args:
            width (int)
            height (int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width to value

        Args:
            value (int): width of rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height to value

        Args:
            value (int): height of rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates and return area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates and return perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + self.__height * 2)

    def __str__(self):
        """Prints rectangle with the character #"""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for h in range(self.__height):
            rectangle += ("#" * self.__width) + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """Returns a formal string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
