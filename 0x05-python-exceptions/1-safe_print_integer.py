#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer
    Args:
        value (int): The integer to print
    Returns:
        If a Type or Value Error occurs, returns False
        Otherwise - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
