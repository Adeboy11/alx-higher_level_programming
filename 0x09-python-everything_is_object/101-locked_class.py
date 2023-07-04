#!/usr/bin/python3
"""Creates a locked class."""


class LockedClass:
    """
    Prevents users from instantiating new a Class.
    """

    __slots__ = ["first_name"]
