#!/usr/bin/python3
""" A class that defines a rectangle
"""

class Rectangle:
    """ class rectangle"""
    def __init__(self, width=0, height=0):
        """ Instantiate width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width
        """
        return self.__width

    @property
    def height(self):
        """ height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ set width

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimiter of a rectangle"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2
