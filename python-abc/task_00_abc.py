#!/usr/bin/env python3

from abc import ABC, abstractmethod

# Defining the abstract class


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Implementing the Dog subclass


class Dog(Animal):
    def sound(self):
        return "Bark"

# Implementing the Cat subclass


class Cat(Animal):
    def sound(self):
        return "Meow"
