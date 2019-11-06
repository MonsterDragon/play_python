#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

"""
key的作用是指定一个函数，这个函数用来将序列中的元素转换为可哈希的类型
使用生成器的目的是为了势函数更通用，若要去重的是文本文件，一行的长度很长，文本很大。
"""
a = [{"a": 1}, {"a", 2}, {"a", 3}]
list(dedupe(a, key=lambda k: (k['a'])))
