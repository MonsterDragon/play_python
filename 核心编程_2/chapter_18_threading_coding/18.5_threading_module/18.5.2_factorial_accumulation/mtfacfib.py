#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

import sys
import os

sys.path.append(os.getcwd())

from myThread import MyThread
from time import sleep, ctime

def fib(x):
    sleep(0.005)
    if x<2:
        return 1
    return (fib(x-2) + fib(x-1))

# print(fib(4))

def fac(x):
    sleep(0.1)
    if x<2:
        return 1
    return x*fac(x-1)

def sum_fun(x):
    sleep(0.1)
    if x<2:
        return 1
    return x+sum_fun(x-1)

funcs = [fib, fac, sum_fun]
n = 12

def main():
    nfuncs = range(len(funcs))

    print("****SINGLE THREAD****")
    for i in nfuncs:
        print("starting", funcs[i].__name__, "at: ", ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, "finished at: ", ctime())

    print("\n****MUTIPLE THREADS****")
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], funcs[i].__name__, n)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())

    print("all Done")

if __name__ == "__main__":
    main()
