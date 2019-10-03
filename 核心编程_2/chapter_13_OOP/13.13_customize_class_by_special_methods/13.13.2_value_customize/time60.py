#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

class Time60(object):
    def __init__(self, hr, mi):
        self.hr = hr
        self.mi = mi

    def __str__(self):
        return %d:%d % (self.hr, self.mi)

    __repr__ = __str__

    def __add__(self, other):
        return self.__class__(self.hr+other.hr, self.mi+other.mi)
 
    def __iadd__(self, other):
        self.hr += other.hr
        self.mi += other.mi
        return self
