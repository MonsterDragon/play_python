#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from random import choice

class RandSeq(object):
    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        return self

    def __next__(self):
        return choice(self.data)

if __name__ == "__main__":
    rand = RandSeq([1, 3, 5, 2])
    # next(rand)
    # next(rand)
    # next(rand)
    # next(rand)
    # next(rand)
    print(rand.__next__())
    print(rand.__next__())
    print(rand.__next__())
    print(rand.__next__())
    print(rand.__next__())
