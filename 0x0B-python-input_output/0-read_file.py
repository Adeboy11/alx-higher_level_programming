#!/usr/bin/python3
"""a function that reads from a file """

def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename: filename
    Raises
        Exception: when the file can be opened
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end='')
