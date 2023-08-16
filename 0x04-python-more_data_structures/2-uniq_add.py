#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_ints = list(set(my_list))
    summ = 0
    for i in range(len(uniq_ints)):
        summ += uniq_ints[i]
    return summ
