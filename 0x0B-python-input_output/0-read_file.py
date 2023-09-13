#!/usr/bin/python3
"""module to read a text file"""


def read_file(filename=""):
    """read a text file and print it"""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="");
