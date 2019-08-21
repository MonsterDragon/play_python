#! /usr/bin/env python
"""
displayNumType_evolution.py - faster program
"""

def displayNumTpye(num):
    print("%d is a" % num)
    if isinstance(num, int):
        print("number of %s" % type(num).__name__)
    else:
        print("not an int at all")

if __name__ == "__main__":
    displayNumTpye(1)
