#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except Exception:
        return False

print(type(filter(is_int, values))) # filter创建了一个迭代器
ivals = list(filter(is_int, values))
print(ivals)
