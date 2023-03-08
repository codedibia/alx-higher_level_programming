#!/usr/bin/python3
def uppercase(str):
    UC = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            UC += chr(ord(c) - 32)
        else:
            UC += c
    print("{}\n".format(UC))
