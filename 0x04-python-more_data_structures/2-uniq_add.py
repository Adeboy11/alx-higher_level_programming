#!/usr/bin/python3
def uniq_add(my_list=[]):
    one = set(my_list)
    result = 0
    for i in one:
        result += i
    return result
