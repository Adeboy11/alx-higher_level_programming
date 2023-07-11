#!/usr/bin/python3
"""A function to check a a class."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a class.

    Args:
        obj (any): The obj to check.
        a_class (type): The class match to the type of obj to.
    Returns:
        If obj is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
