#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

import os
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            # yield line, previous_lines
            # previous_lines.append(line)
            previous_lines.append(line)
    return previous_lines

if __name__ == "__main__":
    file_name = os.path.join(os.getcwd(), "00_main_content.txt")
    with open(file_name, 'r') as f:
        # for prevlines in search(f, 'deque', 3):
        #     for pline in prevlines:
        #         print(pline, end='')
        prevlines = search(f, 'deque', 3)
        print(prevlines)
