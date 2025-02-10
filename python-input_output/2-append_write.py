#!/usr/bin/python3
'''Append File'''


def append_write(filename="", text=""):
    '''Function that appends a string'''
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
