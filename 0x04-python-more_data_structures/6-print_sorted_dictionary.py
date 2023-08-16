#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    let = list(a_dictionary.keys())
    let.sort()
    for i in let:
        print("{}: {}".format(i, a_dictionary[i]))
