#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_lists = []
    for i in range(0, list_length):
        try:
            divs = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divs = 0
        except ZeroDivisionError:
            print("division by 0")
            divs = 0
        except IndexError:
            print("out of range")
            divs = 0
        finally:
            new_lists.append(div)
    return (new_lists)
