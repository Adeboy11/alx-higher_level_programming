#!/usr/bin/python3
"""inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """if an object is an instance or inherited of a class.

    Args:
        obj (any): The obj to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
