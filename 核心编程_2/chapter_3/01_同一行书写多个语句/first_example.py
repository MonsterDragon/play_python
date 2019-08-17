# /usr/bin/env python3
'''
通过obj.__doc__来获取文档注释
'''
import sys; x = "foo"; sys.stdout.write(x + '\n')
print(sys.__doc__)
print(__name__)
