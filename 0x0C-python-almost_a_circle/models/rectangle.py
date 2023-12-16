#!/usr/bin/python3
"""_summary_    """

from models.base import Base

class Rectangle(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    def __init__(self, width, height, x = 0, y = 0, id=None):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """_summary_
        """
        return self.__width
        
    @width.setter
    def width(self, value):
        """_summary_

        Args:
            value (int): width of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an int")
        if value <= 0:
            raise ValueError("width must be > 0")
            self.__width = value
            
    @property
    def height(self):
        """_summary_
        """
        return self.__height
        
    @height.setter
    def height(self, value):
        """_summary_

        Args:
            value (int): height of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be int")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """_summary_
        """
        return self.__x
        
    @x.setter
    def x(self, value):
        """_summary_

        Args:
            value (int): the horizontal position
        """
        if not isinstance(value, int):
            raise TypeError("x must be an int")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """_summary_
        """
        return self.__y
        
    @y.setter
    def y(self, value):
        """_summary_

        Args:
            value (int): the vertical position
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """_summary_
        """
        return self.height * self.width
    
    def display(self):
        """_summary_
        """
        for _ in range(self.y):
            print('')
        for _ in range(self.height):
            print(' '*self.x + '#' * self.width)
    
    def __str__(self):
        """_summary_
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, 
                                                       self.x, 
                                                       self.y, 
                                                       self.width, 
                                                       self.height)

    def update(self, *args, **kwarg):
        """_summary_
        """
        if args:
            for i, k in enumerate(args):
                if i == 0:
                    self.id = k
                elif i == 1:
                    self.width = k
                elif i == 2:
                    self.height = k
                elif i == 3:
                    self.x = k
                elif i == 4:
                    self.y = k
                else:
                    continue
        elif len(kwarg) > 0:
            for k, v in kwarg.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """_summary_
        """
        rec = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

        return rec
