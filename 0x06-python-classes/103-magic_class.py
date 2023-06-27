#!/usr/bin/python3
"""rep of a Sq"""

import math

class MagicClass:
    """rep of a Sq"""

    def __init__(self, radius=0):
        """Initialize a new square.

        Args:
            size (int): the square. 
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """rep of a Sq"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """rep of a Sq"""
        return (2 * math.pi * self.__radius)
