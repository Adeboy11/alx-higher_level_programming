#!/usr/bin/python3
def search_replace(my_list, search, replace):
    repl = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            repl.append(replace)
        else:
            repl.append(my_list[i])
    return repl
