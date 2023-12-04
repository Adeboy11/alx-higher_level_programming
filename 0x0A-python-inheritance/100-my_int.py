#!/usr/bin/python3
""" class MyInt that inherits from int:
"""

class MyInt(int):
    """_summary_

    Args:
        int (_type_): _description_
    """
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
