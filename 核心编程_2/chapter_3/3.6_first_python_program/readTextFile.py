#! /usr/bin/env python3

"readTextFile.py -- read and display text file"

import os

ls = os.linesep

# get filename
fname = input("Enter filename:")
print()

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError as e:
    print("the e is:{}".format(e))
    print("{} file opne error").format(fname)
else:
    # display contents to the screen 
   for eachline in fobj:
       print(eachline)
   fobj.close()
