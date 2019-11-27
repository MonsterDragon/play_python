#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from collections import deque
class lineistory(object):
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1): # 1表示下标起始位置
            self.history.append((lineno, line))
            yield

    def clear(self):
        self.history.clear()

with open('someone.txt', 'r') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
