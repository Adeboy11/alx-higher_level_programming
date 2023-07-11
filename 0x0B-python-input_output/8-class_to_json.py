#!/usr/bin/python3
"""a Python class-to-JSON function."""


def class_to_json(obj):
    """the dictionary represntation of a simple data structure."""
    return obj.__dict__
