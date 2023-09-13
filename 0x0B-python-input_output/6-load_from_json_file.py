#!/usr/bin/python3
"""module to read a text file"""
import json


def load_from_json_file(filename):
    """read a text file and print it"""
    with open(filename, mode='r', encoding="utf-8") as file:
        return json.load(file)
