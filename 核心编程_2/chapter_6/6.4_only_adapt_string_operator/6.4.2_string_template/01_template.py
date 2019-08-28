#! /usr/bin/env python3

"""
string模块的template模板
"""
from string import Template

s = Template("There are ${howmany} ${lang} Quotation Symbols")
print(s.substitute(lang="Python", howmany=3))
