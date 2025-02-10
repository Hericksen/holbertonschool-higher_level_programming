#!/usr/bin/python3
import json
'''Save Object to a file'''


def save_to_json_file(my_obj, filename):
    '''function that writes an Object to a text file, using a JSON representation'''
    with open(filename, "w") as outfile:
        json.dump(my_obj, outfile)
