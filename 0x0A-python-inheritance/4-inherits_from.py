#!/usr/bin/python3

""" to check whether  object is an instance of a class that
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    if none is met
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
