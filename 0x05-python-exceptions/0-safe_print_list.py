#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list

    Args:
        my_list: list to print elements from
        x (int): number of elements of my_list to print

    Returns:
        The number of elements printed
    """
    lst = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            lst += 1
        except IndexError:
            break
    print("")
    return (lst)
