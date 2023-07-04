#!/usr/bin/python3
"""A function that prints square."""


def print_square(size):
    """Prints a sq with the # char.

    Args:
        size (int): The dimension of the sq.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
