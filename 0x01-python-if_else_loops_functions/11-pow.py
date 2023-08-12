#!/usr/bin/python3
def pow(a, b):
    if b > 0:
        x = a
    if b < 0:
        x=1/a
    for n in range(1, b):
        x *= x
    return x
