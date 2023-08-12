#!/usr/bin/python3
def uppercase(str):
    difference = ord('A')-ord('a')
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            letter = chr(ord(letter) + difference)
        print("{}".format(letter), end="")
    print("")
