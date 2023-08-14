#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    prototype=my_list[:]
    if idx < 0:
        return prototype
    if idx > len(my_list) - 1:
        return prototype
    prototype[idx] = element
    return prototype

