#!/usr/bin/python3
"""module to read a text file"""
import json


def save_to_json_file(my_obj, filename):
    """read a text file and print it"""
    with open(filename, mode='w', encoding="utf-8") as file:
        json.dump(my_obj, file)
