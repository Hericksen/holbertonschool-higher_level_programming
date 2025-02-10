#!/usr/bin/python3
'''Write file'''


def write_file(filename="", text=""):
    "Function that writes a string to a text file (UTF8)"
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
