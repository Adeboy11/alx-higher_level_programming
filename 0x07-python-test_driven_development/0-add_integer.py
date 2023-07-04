#!/usr/bin/python3
"""an add function."""


def add_integer(a, b=98):
    """Returns an int addition of a and b.

    Float arguments are typecaste to ints before addition.

    Raises:
        TypeError: If a or b is not integer or not float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
