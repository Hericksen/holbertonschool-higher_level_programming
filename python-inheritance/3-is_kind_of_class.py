#!/usr/bin/python3
'''Module 3-is_kind_of_class'''


def is_kind_of_class(obj, a_class):
    '''Returns True if the object is an instance of, or if the object
    is an instanceof a class that inherited from, the specified class'''
    return isinstance(obj, a_class)
