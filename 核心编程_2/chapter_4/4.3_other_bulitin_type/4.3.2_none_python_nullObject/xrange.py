#! /usr/bin/env python3

"""
xrange -- define xrange function
"""

def xrange(dig):
    n = 0
    while n < dig:
        yield n
        n += 1

if __name__ == "__main__":
    print(xrange(5))
    print(xrange(5).__next__)
    print(next(xrange(5)))
