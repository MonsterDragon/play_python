#! /usr/bin/env python3
# -*- coding=utf-8 -*-

def testit(func, *args, **kwargs):
    try:
        retval = func(*args, **kwargs)
        result = (True, retval)
    except Exception as e:
        result = (False, str(e))
    return result

def test():
    funcs = (int, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print("_" * 20)
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            print(retval)
            if retval[0]:
                print("%s(%s)= %s" % (eachFunc.__name__, eachVal, retval[1]))

if __name__ == "__main__":
    test()
