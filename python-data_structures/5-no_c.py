#!/usr/bin/python3
def no_c(my_string):
    new_string = ""  # Initialize an empty string to store the result
    for char in my_string:  # Iterate through each character in the input string
        if char != 'c' and char != 'C':  # Add to new_string if not 'c' or 'C'
            new_string += char
    return new_string
