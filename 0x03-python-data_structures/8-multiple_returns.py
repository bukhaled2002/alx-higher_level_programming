#!/usr/bin/python3
def multiple_returns(sentence):
    fchar=None
    if len(sentence) != 0:
        fchar = sentence[-1]
    return (len(sentence),fchar)
