#!/usr/bin/python
def uppercase(str):
    difference = ord('A')-ord('a')
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            print("{}".format(chr(ord(letter) + difference)), end="")
        else:
            print("{}".format(chr(ord(letter))), end="")
