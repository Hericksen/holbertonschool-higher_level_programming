#!/usr/bin/env python3
# Define the mixins
class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Define the Dragon class that inherits from both mixins


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
