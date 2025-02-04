#!/usr/bin/python3
'''Module 2-is_same_class'''


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class, otherwise False."""
    return type(obj) is a_class
