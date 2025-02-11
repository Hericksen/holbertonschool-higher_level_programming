#!/usr/bin/python3
"""Module to convert CSV to JSON."""


import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to JSON and writes it to data.json"""

    try:
        """open the CSV files"""
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File {csv_filename} not  found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
