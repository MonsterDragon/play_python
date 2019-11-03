#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({})'.format(self.name)

if __name__ == "__main__" :
    q = PriorityQueue()
    # print(Item('foo'))
    q.push(Item('foo'), 1)
    print(q._queue)
    q.push(Item('bar'), 5)
    print(q._queue)
    q.push(Item('spam'), 4)
    print(q._queue)
    q.push(Item('grok'), 1)
    print(q._queue)
    print(q.pop())
    print(q._queue)
    print(q.pop())
    print(q._queue)
    print(q.pop())
    print(q._queue)
    print(q.pop())
    print(q._queue)
