#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.captalize()
        else:
            return word
    return replace
