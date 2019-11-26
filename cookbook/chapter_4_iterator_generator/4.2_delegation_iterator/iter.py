#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

class Node(object):
    def __init__(self, value):
        self._value = value
        print(self._value)
        self._children = []

    # def __repr__(self):
    #     return 'Node({})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    print("list", root._children)
    for ch in root:
        # print(ch)
        print(ch._value)
