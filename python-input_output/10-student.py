#!/usr/bin/python3
'''Student to JSON'''


class Student:
    '''Constructor'''

    def __int__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    '''Retrive dict representation'''

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            return {x: getattr(self, x) for x in attrs
                    if hasattr(self, x)}
        return self.__dict__
