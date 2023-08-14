#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    i = 0
    for n in range(len(my_list)):
        if i < my_list[n]:
            i = my_list[n]
        else:
            continue
    return i
