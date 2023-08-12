#!/usr/bin/python3
lis = []
for digit1 in range(0,10):
    for digit2 in range(digit1,10):
        if f"{digit1}{digit2}" != f"{digit2}{digit1}":
            lis.append(int(f"{digit1}{digit2}"))
for x in lis:
    if x != lis[-1]:
        print("{:0>2d}".format(x),end=", ")
    else:
        print("{:0>2d}".format(x))
