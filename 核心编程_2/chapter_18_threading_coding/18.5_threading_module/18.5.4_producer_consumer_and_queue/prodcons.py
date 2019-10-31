#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

import sys
import os
from imp import reload

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")) +
"/18.5.2_factorial_accumulation")

reload(sys)

from random import randint
from time import sleep
from queue import Queue
from myThread import MyThread

def writeQ(queue):
    print("producing object for Q...")
    queue.put('xxx', 1)
    print("size now ", queue.qsize())

def readQ(queue):
    val = queue.get(1)
    print("consumed object from Q... size now: ", queue.qsize())

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(1, 3))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], funcs[i].__name__, q, nloops)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print("all Done")

if __name__ == "__main__":
    main()
