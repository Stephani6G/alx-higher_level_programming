#!/usr/bin/python3

"""to check if object is an instance of a class
or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instance of a class
    or a class that the class in question inherits, otherwise false
    """
    return (isinstance(obj, a_class))
