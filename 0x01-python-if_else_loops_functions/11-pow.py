#!/usr/bin/python3
def pow(a, b):
    x = a
    for n in range(1,b):
        x *= x
    return x
