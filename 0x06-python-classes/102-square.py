#!/usr/bin/python3
"""rep of a Sq"""

class Square:
    """rep of a Sq"""
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of square.
            position (int, int): position of the new square.
        """
        self.size = size

    @property
    def size(self):
        """rep of a Sq"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """rep of a Sq"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """rep of a Sq"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """rep of a Sq"""
        return self.area() == other.area()

    def __ne__(self, other):
        """rep of a Sq"""
        return self.area() != other.area()

    def __lt__(self, other):
        """rep of a Sq"""
        return self.area() < other.area()

    def __le__(self, other):
        """rep of a Sq"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """rep of a Sq"""
        return self.area() > other.area()

    def __ge__(self, other):
        """rep of a Sq"""
        return self.area() >= other.area()
