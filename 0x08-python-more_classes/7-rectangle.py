#!/usr/bin/python3
""" A class that defines a rectangle """

class Rectangle:
    """ class rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Instantiate width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """ returns area rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of a rectangle """
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ prints rectangle with character #
        """
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.__width)]) for j in range(self.__height)]))

    def __repr__(self):
        """ prints a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints delete message when an instance of Rectangle is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
