#!/usr/bin/python3
def magic_calculation(a, b):
    """magic calculation
    Args:
        a: argument 1
        b: argument 2

    Returns results
    """
    results = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            results += a ** b / i
        except Exception:
            results = b + a
            break
    return results
