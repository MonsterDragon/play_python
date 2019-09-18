#! /usr/bin/env python3
# -*- coding=UTF-8 -*-

from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print("[%s] %s called" % (ctime(), func.__name__))
        func()
    return wrappedFunc

@tsfunc
def foo():
    print("hello!")

if __name__ == "__main__":
    foo()
    sleep(2)
    for i in range(3):
        foo()
        sleep(1)
