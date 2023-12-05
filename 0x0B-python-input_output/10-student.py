#!/usr/bin/python3
""" the student class
"""

class Student:
    """ creates student instances """

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        obj = self.__dict__.copy()

        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for atr_s in range(len(attrs)):
                for atr_y in obj:
                    if attrs[atr_s] == atr_y:
                        d_list[atr_y] = obj[atr_y]
            return d_list

        return obj
