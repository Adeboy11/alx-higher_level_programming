#!/usr/bin/python3
""" this returns a dictionary with a simple
data structure for a JSON serialization of an object
"""

def class_to_json(obj):
    """ Retuns the dictionary description of an obj """

    ans = {}
    if hasattr(obj, "__dict__"):
        ans = obj.__dict__.copy()
    return ans
