#!/usr/bin/python3
'''Mode - 7-base_geometry'''


class BaseGeometry:
    '''Base Geometry class'''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''fnc fir int validator'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
