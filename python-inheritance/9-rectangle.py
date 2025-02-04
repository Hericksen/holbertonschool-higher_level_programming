#!/usr/bin/python3
'''Mode - 9-base_geometry'''


class BaseGeometry:
    '''Base Geometry class'''

    def area(self):
        '''fnc of area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''fnc fir int validator'''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    '''Rectangle class'''

    def __init__(self, width, height):
        '''def for init square'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''fnc for area'''
        return self.__width * self.__height

    def __str__(self):
        '''fnc for print'''
        return f"[Rectangle] {self.__width}/{self.__height}"
