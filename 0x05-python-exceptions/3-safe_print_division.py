#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        divs = a / b
    except (TypeError, ZeroDivisionError):
        divs = None
    finally:
        print("Inside result: {}".format(div))
    return (divs)
