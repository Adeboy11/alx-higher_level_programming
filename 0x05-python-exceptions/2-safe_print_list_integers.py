#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints an x integer
    Args:
        my_list (int): The integer to print
        x: number of elements to accessed
    Returns:
        Prints x number of elements
    """
    idx = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            idx += 1

    print()
    return (idx)
