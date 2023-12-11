#!/usr/bin/python3
"""_summary_    """

from rectangle import Rectangle

class Square(Rectangle):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    def __init__(self, size, x=0, y=0, id=None):
        """_summary_

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """_summary_
        """
        return self.width
    
    @size.setter
    def size(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, 
                                                 self.x, 
                                                 self.y, 
                                                 self.width)
    
    def update(self, *args, **kwargs):
        """_summary_
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                if k == 1:
                    self.size = v
                if k == 2:
                    self.x = v
                if k == 3:
                    self.y = v
                continue
        elif len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id == v
                elif k == "size":
                    self.width = v
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
                else:
                    break
    def to_dictionary(self):
        """_summary_
        """
        rec = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
        return rec
