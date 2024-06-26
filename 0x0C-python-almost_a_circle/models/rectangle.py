#!/usr/bin/python3
""" Module contains class Rectange """

from models.base import Base


class Rectangle(Base):
    """ This class inherits from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Intialiazes rectangle instances """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ access to width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets value of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ access to height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets value of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ access to x """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets value of x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ access to y """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets value of y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.__width * self.__height
