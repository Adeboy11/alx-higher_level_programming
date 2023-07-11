#!/usr/bin/python3
"""an inherited list class MyList."""

class MyList(list):
    """prints sorted printing for list class."""

    def print_sorted(self):
        """Print a list in ascending order."""
        print(sorted(self))
