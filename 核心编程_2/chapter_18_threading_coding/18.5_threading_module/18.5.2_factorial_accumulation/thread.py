#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

import threading
from time import sleep, ctime

loops = (4, 2)

class MyThread(threading.Thread):
    def __init__(self, func, name='', *args):
        threading.Thread.__init__(self)
        self.func = func
        self.name = name
        self.args = args

    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print("start loop: ", nloop, "at: ", ctime())
    sleep(nsec)
    print("loop: ", nloop, "at: ", ctime())

def main():
    print("starting at: ", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, loop.__name__, i, loops[i])
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("all Done at: ", ctime())

if __name__ == "__main__":
    main()
