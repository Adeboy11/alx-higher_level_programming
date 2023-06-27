#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a sq"""

    def __init__(self, size):

        """Initialize a new sq

        Args:
            size (int): size of the new square.
        """

        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the size of sq"""
    
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of sq"""
        
        return (self.__size * self.__size)

    def my_print(self):
        """Print sq with # character."""
        
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
