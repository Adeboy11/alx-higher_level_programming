#!/usr/bin/python3
"""a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end text file.

    Args:
        filename (str): name of the file to append to.
        text (str): str to append.
    Returns:
        The number of characters to append.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
