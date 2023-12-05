#!/usr/bin/python3
""" Function that returns an object from JSON
"""
import json

def from_json_string(my_str):
    """ Returns an object from a JSON

    Args:
        my_str: JSON representation
    Raises:
        Exception: when the string can't be decoded
    """
    return json.loads(my_str)
