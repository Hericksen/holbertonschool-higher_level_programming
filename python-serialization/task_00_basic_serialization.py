#!/usr/bin/python3
"""" Module for serialize and deserialize operations."""


import json


def serialize_and_save_to_file(data, filename):
    """Serialize data and save it to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
