#!/usr/bin/python3

def safe_print_division(a, b):
    """a func to divide a by b
    Args:
        a: argument 1
        b: argument 2

    Returns the division of a by b
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
