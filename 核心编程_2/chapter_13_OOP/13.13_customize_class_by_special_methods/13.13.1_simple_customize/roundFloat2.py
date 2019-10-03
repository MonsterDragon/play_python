#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), "Value must be a float!"
        self.value = val
    def __str__(self):
        return "%.2f" % self.value
    __repr__ = __str__

if __name__ == "__main__":
    rfm = RoundFloatManual(5.12312)
    print(rfm)
