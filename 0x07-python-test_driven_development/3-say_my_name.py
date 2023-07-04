#!/usr/bin/python3
"""a function that prints name."""


def say_my_name(first_name, last_name=""):
    """Prints name.

    Args:
        first_name (str): The 1st name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
