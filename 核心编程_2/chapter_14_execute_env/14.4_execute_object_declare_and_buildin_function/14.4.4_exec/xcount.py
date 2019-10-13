#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

x = 0
expr = """
print("x is currently:", x)
while x < 5:
    x += 1
    print("incrementing x to:", x)
"""
def func():
    exec(expr)
    exec(expr, {'x': 3})

if __name__ == "__main__":
    func()
