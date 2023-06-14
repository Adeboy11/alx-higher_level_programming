#!/usr/bin/python3
def uniq_add(my_list=[]):
    first = set(my_list)
    nexts = 0
    for i in first:
        nexts += i
    return nexts
