#!/usr/bin/python3
'''Student to JSON'''


class Student:
    '''Constructor'''
    def __int__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    '''Retrieve dict representation'''
    def to_json(self):
        return self.__dict__
