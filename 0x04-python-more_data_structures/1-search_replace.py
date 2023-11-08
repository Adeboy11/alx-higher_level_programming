#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rep = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            rep.append(replace)
        else:
            rep.append(my_list[i])
    return rep
