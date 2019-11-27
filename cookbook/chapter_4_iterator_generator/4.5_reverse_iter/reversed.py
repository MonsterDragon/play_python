#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

class Countdown(object):
    def __init__(self):
        self.start = start
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
