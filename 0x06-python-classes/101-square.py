#!/usr/bin/python3
"""rep of a Sq"

class Square:
    """rep of a Sq"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): size of a square.
            position (int, int): position of a square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """rep of a Sq"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """rep of a Sq"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """rep of a Sq"""
        return (self.__size * self.__size)

    def my_print(self):
        """rep of a Sq"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
    """Define print rep of a Sq"""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
