#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

import os

def execvp(name):
    for i in name:
        print(i)

ret = os.fork()
if ret == 0:
    execvp('xbill')
else:
    os.wait()
