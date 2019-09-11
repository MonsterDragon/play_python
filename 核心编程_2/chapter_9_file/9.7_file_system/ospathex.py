#! /usr/bin/env python3
# -*- coding=UTF-8 -*-

import os

for tmpdir in ('/tmp', r'c: \tmp'):
    if os.path.isdir(tmpdir):
        break
else:
    print("no tmp directory available")
    tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print("***current temporary directory***")
    print(cwd)

    print("***creating example directory***")
    os.mkdir("example")
    os.chdir("example")
    cwd = os.getcwd()
    print("***new working directory: ")
    print(cwd)
    print("***original directory listing: ")
    print(os.listdir(cwd))

    print("***creating test file***")
    fobj = open('test', 'w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print("***updated directory listing: ")
    print(os.listdir(cwd))
    
    print("***rename 'test' to 'filetest.txt'")
    os.rename('test', 'filetest.txt')
    print("***updating directory listing: ")
    print(os.listdir(cwd))

    path = os.path.join(cwd, os.listdir(cwd)[0])
    print("***full file pathname***")
    print(path)
    print("***(pathname, basename) ==")
    print(os.path.split(path))
    print("***(filename, extention) ==")
    # print(os.path.splitext(list(os.path.split(path))))

    print("***displaying file contents***")
    fobj = open(path)
    for eachLine in fobj:
        print(eachLine)
    fobj.close()

    print("***deleting test file")
    os.remove(path)
    print("***updated directory listing: ")
    print(os.listdir(cwd))
    os.chdir(os.pardir)
    print("***deleting test directory***")
    os.rmdir('example')
    cur_dir = os.getcwd()
    print(cur_dir)
    print("done***")
    print(os.listdir())
