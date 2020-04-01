#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import urllib2

# response = urllib2.urlopen("http://www.baidu.com/")
# html = response.read()

req = urllib2.Request("http://www.baidu.com/") # urllib2.Request类
response = urllib2.urlopen(req) # response类似于一个文件对象
html = response.read()
print html
