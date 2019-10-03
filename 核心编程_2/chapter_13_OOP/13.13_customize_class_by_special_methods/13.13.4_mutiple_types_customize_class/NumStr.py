#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

class NumStr(object):
    def __init__(self, num=0, string=''):
        self.n = num
        self.s = string

    def __str__(self):
        return "[%d::%r]" % (self.n, self.s)

    __repr__ == __str__

    def __add__(self, other):
        if isinstance(other, NumStr):
            return self.__class__(self.n+other.n, self.s+other.s)
        else:
            raise TypeError, "Illegal arguement type for built-in operation"

    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(self.n*num, self.s*num)
        else:
            rasie TypeError, "Illegal arguement type for built-in operation"

    def __nonzero__(self):
        return self.n or len(self.s)

    def __norm_cval(self, cmpres):
        return cmp(cmpress,  0)

    def __cmp__(self, other):
        return self.__norm_cval(cmp(self.n, other.n)) +
    self.__norm_cval(cmp(self.s, other.s))

if __name__ == "__main__":




