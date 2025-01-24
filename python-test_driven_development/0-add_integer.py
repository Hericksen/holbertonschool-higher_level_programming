#!/usr/bin/python3
"""
This module provides basic arithmetic operations with input validation.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, casting them to integers if necessary.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, default is 98, must be an integer or float.

    Returns:
        int: The result of adding a and b as integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    # Cast to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b
