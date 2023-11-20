#!/usr/bin/python3
def safe_function(fct, *args):
    """a func to raise exception
    Args:
        fct: argument 1
        *args: argument 2

    Returns results
    """
    import sys
    try:
        results = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        results = None

    return (results)
