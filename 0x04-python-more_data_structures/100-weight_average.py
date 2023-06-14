#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    difference = 0
    for i in my_list:
        average += i[0] * i[1]
        difference += i[1]
    return float(average / difference)
