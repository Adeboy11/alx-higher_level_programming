#!/usr/bin/python3

""" base class    """
import json
import csv
import turtle

class Base:
    """_summary_
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """_summary_

        Args:
            id (int): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """_summary_

        Args:
            list_dictionaries (_type_): _description_
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        toJson = json.dumps(list_dictionaries)
        return toJson
    @staticmethod
    def save_to_file(cls, list_objs):
        """_summary_

        Args:
            list_objs (_type_): _description_
        """
        cls_file = "{}.json".format(cls.__name__)
        with open(cls_file, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_dict = []
                for objs in list_objs:
                    json_dict.append(objs.to_dictionary())
                json.write(Base.to_json_string(json_dict))

    def from_json_string(json_string):
        """_summary_

        Args:
            json_string (_type_): _description_
        """
        if json_string is None or json_string == "[]":
            return []
        return json.load(json_string)


    @classmethod
    def create(cls, **dictionary):
        """_summary_
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """_summary_
        """
        files = "{}.json".format(__name__)
        try:
            with open(files, 'r') as json_f:
                list_dict = Base.from_json_string(json_f.read())
                list_of_instances = []
                for i in list_dict:
                    list_of_instances.append(cls.create(**i))
                return list_of_instances
        except FileNotFoundError:
            return []
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """_summary_

        Args:
            list_objs (_type_): _description_
        """
        files = "{}.json".format(cls.__name__)
        with open(files, 'w') as csv_f:
            if list_objs is None or list_objs == []:
                csv_f.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    f_names = ["id", "width", "height", "x", "y"]
                else:
                    f_names = ["id", "size", "x", "y"]
                f_write = csv.Dictwriter(csv_f, f_names=f_names)

            for obj in list_objs:
                f_write.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """_summary_
        """
        file_name = "{}.json".format(__name__)

        try:
            with open(file_name, 'r') as csv_f:
                if cls.__name__ == "rectangle":
                    f_names = ["id", "width", "height", "x", "y"]
                else:
                    f_names = ["id", "size", "x", "y"]
                f_write = csv.Dictwriter(csv_f, f_names=f_names)

                list_dict = []
                con_dict = []
                for obj in f_write:
                    for k, v in obj.items():
                        con_dict[k] = int(v)

                l_dict = list_dict
                list_of_instances = []

                for i in l_dict:
                    list_of_instances.append(cls.create(**i))
                return list_of_instances
        except FileNotFoundError:
            return "[]"

    @staticmethod
    def draw(list_rectangles, list_squares):
        """_summary_

        Args:
            list_rectangles (_type_): _description_
            list_squares (_type_): _description_
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("orange")
        turt.pensize(4)
        turt.shape("turtle")

        for lists in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(lists.x, lists.y)
            turt.down()
            for _ in range(2):
                turt.forward(lists.width)
                turt.left(90)
                turt.forward(lists.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("red")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
