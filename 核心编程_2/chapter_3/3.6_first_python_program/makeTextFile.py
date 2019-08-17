#! /usr/bin/env python3

"makeTextFile.py -- create text file"

import os

ls = os.linesep

# get filename
while True:
    fname = input("> ")
    if os.path.exists(fname):
        print("Error: {} is already exists".format(fname))
    else:
        break

# get file content lines
content_lines = []
print("\nEnter lines('.' by itself to quit.\n)")

# loop until user terminates input
while True:
    line = input("> ")
    if line == ".":
        break
    else:
        content_lines.append(line)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(["%s%s" % (x, ls) for x in content_lines])
fobj.close()
print("done")
