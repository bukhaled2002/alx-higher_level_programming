#!/usr/bin/python3
def simple_delete(a_dictionary: dict, key=""):
    a_dictionary.__delitem__(key) if a_dictionary.__contains__(key) else None
    return a_dictionary
