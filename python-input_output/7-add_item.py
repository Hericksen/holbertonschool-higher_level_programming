#!/usr/bin/python3
'''Load, add, save'''
import json
import sys


def save_to_json_file(my_obj, filename):
    '''function that writes an Object to a text file'''
    with open(filename, "w") as outfile:
        json.dump(my_obj, outfile)


def load_from_json_file(filename):
    '''function that creates an Object from a “JSON file”'''
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    filename = "add_item.json"
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
