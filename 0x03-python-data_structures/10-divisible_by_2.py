#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    l_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            l_list.append(True)
        else:
            l_list.append(False)
    return l_list
