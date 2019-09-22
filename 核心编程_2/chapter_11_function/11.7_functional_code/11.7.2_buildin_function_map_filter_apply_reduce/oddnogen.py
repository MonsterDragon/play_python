#! /usr/bin/env python3
# -*- coding=UTF-8 -*-

from random import randint

# all_nums = [randint(1, 99) for i in range(9)]
# filter_nums = filter(lambda x: x%2, all_nums)
# print([i for i in filter_nums])
print([n for n in [randint(1, 99) for i in range(9)] if n%2])
