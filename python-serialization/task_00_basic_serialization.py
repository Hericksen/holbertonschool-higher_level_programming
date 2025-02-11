#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"Data serialized and saved to '{filename}'.")
    except Exception as e:
        print(f"Error serializing data: {e}")


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
