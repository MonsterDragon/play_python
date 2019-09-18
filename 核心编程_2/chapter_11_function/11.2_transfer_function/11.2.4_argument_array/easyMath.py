#! /usr/bin/env python3
# -*- coding=UTF-8 -*-

from operator import add, sub
from random import randint, choice

ops = {'+': add, '-': sub}
MAXTRIES = 2

def doprob():
    op = choice('+-')
    nums = [randint(1,10) for i in range(2)]
    nums.sort(reverse =True)
    ans = ops[op](*nums)
    pr = "%d %s %d=" % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(input(pr)) == ans:
                print("correct!")
                break
            elif oops == MAXTRIES:
                print("answer\n%s%d" % (pr, ans))
            else:
                print("incorrect try again")
                oops += 1
        except Exception:
            print("Invalid input try again")

def main():
    while True:
        doprob()
        try:
            opt = input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except Exception:
            break

if __name__ == "__main__":
    main()
