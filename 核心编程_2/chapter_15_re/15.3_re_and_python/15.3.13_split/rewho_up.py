#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import os
import re
import sys

def main(file_name):
    f = os.popen("who")
    for eachLine in f:
        print re.split("\s\s+|\t", eachLine)

if __name__ == "__main__":
    main(sys.argv[1])
