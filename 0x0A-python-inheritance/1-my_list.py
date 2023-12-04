#!/usr/bin/python3
"""class MyList that inherits from list
"""

class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """prints the list, that is sorted
        """
        print(sorted(self))
