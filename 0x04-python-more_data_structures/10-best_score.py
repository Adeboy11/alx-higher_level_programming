#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    returns = list(a_dictionary.keys())[0]
    dicts = a_dictionary[returns]
    for i, j in a_dictionary.items():
        if j > dicts:
            dicts = j
            returns = i
    return (returns)
