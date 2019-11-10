#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from collections import namedtuple

Stock = namedtuple("Stock", ['name', 'shares', 'price', 'date', 'time'])

stock_prototype = Stock('', 0, 0.0, None, None)

def dict_to_stock(s):
    # _replace()方法可以作为一种简单的方法填充具有可选或缺失字段的命名元组，并对相应的值做替换
    return stock_prototype._replace(s**)
