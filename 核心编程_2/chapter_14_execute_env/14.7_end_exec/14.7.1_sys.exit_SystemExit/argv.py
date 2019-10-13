#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

import sys

def usage():
    print("At least 2 arguments (incl and cmd name).")
    print("usage: argv.py arg1 arg2")
    sys.exit(1)

argc = len(sys.argv)

if argc < 3:
    usage()
