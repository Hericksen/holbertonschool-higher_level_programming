#!/usr/bin/python3
'''Student to JSON'''


class Student:
    '''Constructor'''

    def __int__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    '''Retrive dictonnary representation'''

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student instance'''
        for key in json:
            self.__dict__[key] = json[key]
