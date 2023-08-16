#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    b_list = my_list.copy()
    for i in range(len(b_list)):
        b_list[i] = my_list[i] * number
    return b_list
