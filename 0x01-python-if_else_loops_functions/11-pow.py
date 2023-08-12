#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        x=1/a
    else:
        x=a

    for n in range(1, abs(b)):
        x *= x
    return x
