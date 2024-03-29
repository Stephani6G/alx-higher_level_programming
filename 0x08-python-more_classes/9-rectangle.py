#!/usr/bin/python3

"""
defines a rectangle class Rectangle
"""


class Rectangle:
    """ class rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Gives optional width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """width value an integer
        """
        return self.__width

    @property
    def height(self):
        """height value an integer
        """
        return self.__height

    @width.setter
    def width(self, value):
        """width setter an integer
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter an inetger
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def area(self):
        """ returns rectangle area in integers
	"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns rectangle perimiter an integer value
	"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ return the rectangle with the character #
        """
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.__width)]) for j in range(self.__height)]))

    def __repr__(self):
        """ return a string representation of the rectangle docstring
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
