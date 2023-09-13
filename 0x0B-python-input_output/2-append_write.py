#!/usr/bin/python3
"""module to read a text file"""


def append_write(filename="", text=""):
    """read a text file and print it"""
    with open(filename, mode='a', encoding="utf-8") as file:
        return file.write(text) 
