#!/usr/bin/python3
def multiply_by_2(a_dictionary: dict):
    b_dictionary = a_dictionary.copy()
    new_list = list(b_dictionary.keys())
    for i in new_list:
        b_dictionary[i] = a_dictionary[i]*2
    return b_dictionary
