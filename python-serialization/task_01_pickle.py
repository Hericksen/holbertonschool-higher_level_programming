#!/usr/bin/python3
import pickle
"""1. Pickling Custom Classes"""


class CustomObject:
    """Defines a custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initializes a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes in a formatted manner."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the object and saves it to a file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Loads an object instance"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None
