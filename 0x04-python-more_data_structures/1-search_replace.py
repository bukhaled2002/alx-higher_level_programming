#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_cp = my_list[:]
    list_cp = list(map(lambda x: replace if x == search else x, my_list))
    return list_cp
