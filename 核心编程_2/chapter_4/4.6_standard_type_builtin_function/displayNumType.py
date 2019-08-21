#! /usr/bin/env python

"""
displayNumType - show the statement of isinatnce function
"""

def displayNumType(num):
    print("%d, is" % num)
    if isinstance(num, (int, long, float, complex)):
        print("a number of type:%s" % type(num).__name__)
    else:
        print("not a number at all!")

if __name__ == "__main__":
    displayNumType(3)
