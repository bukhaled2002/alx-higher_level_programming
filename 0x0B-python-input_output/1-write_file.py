#!/usr/bin/python3
"""module to read a text file"""


def write_file(filename="", text=""):
    """read a text file and print it"""
    with open(filename, mode='w', encoding="utf-8") as file:
        return file.write(text)
        
