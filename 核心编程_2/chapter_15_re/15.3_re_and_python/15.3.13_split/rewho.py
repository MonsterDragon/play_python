#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import re
import sys

def main(file_name):
    with open(file_name, 'r') as f:
        for eachLine in f:
            print re.split("\s\s+", eachLine)

if __name__ == "__main__":
    main(sys.argv[1])
