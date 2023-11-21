#!/usr/bin/python3
"""A Magic Class"""

import math


class MagicClass:
    """A magic class representing a circle."""

    def __init__(self, radius=0):
        """Initialize a Magic Class

        Arg:
            radius (float or int): The radius of the new Magic Class.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of Magic Class"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the Magic Class"""
        return (2 * math.pi * self.__radius)
