#!/usr/bin/python3
# 3-print_alphabet.py
for x in range(97, 123):
    if chr(x) != 'q' and chr(x) != 'e':
        print("{}".format(chr(x)), end="")
