#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

import threading
from time import sleep, ctime

loops = [4, 2]

class ThreadFunc(object):

    def __init__(self, func, name='', *args):
        self.name = name
        self.func = func
        self.args = args
        print("*args: ", *args)
        print("args: ", args)

    def __call__(self):
        print("*self.args: ", *self.args)
        self.func(*self.args)

def loop(nloop, nsec):
    print("start loop: ", nloop, "at: ", ctime())
    sleep(nsec)
    print("loop: ", nloop, "at: ", ctime())

def main():
    print("start loop at: ", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, loop.__name__, i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("all Done at: ", ctime())

if __name__ == "__main__":
    main()
