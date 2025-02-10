#!/usr/bin/python3
'''Student to JSON'''


class Student:
    '''Class student'''
    def __int__(self, first_name, last_name, age):
        '''constructior'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieve dictonnary representation'''
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student instance'''
        for key in json:
            self.__dict__[key] = json[key]
