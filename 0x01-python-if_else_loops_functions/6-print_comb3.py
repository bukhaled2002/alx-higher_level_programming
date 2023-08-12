#!/usr/bin/python3
for digit1 in range(0, 10):
    for digit2 in range(digit1, 10):
        if f"{digit1}{digit2}" != f"{digit2}{digit1}":
            if f"{digit1}{digit2}" != "89":
                print("{}".format(int(f"{digit1}{digit2}")), end=", ")
            else:
                print("{:0>2d}".format(int(f"{digit1}{digit2}")))
