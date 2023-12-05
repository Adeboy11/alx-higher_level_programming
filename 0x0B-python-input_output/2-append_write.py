#!/usr/bin/python3
""" A function that appends a text to a file
"""

def append_write(filename="", text=""):
    """ Appends to a text file

    Args:
        filename: filename
        text: text to write

    Raises:
        Exception: when the file can be opened
    """
    with open(filename, 'a', encoding="utf8") as f:
        return f.write(text)
