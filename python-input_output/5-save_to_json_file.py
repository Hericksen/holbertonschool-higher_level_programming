#!/usr/bin/python3
'''Save Object to a file'''
import json


def save_to_json_file(my_obj, filename):
    '''function that writes an Object to a text file'''
    with open(filename, "w") as outfile:
        json.dump(my_obj, outfile)
