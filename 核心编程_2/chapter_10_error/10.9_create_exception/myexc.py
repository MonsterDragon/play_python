#! /usr/bin/env python3
# -*- coding=UTF-8 -*-

import os
import socket
import errno
import types
import tempfile

class NetworkError(IOError):
    pass

class FileError(IOError):
    pass

def updArgs(args, newarg=None):
    """更新异常参数 正常的IOError会返回一个元组的参数"""
    if isinstance(args, IOError):
        myargs = []
        myargs.extend([arg for arg in args])
    else:
        myargs = list(args)

    if newarg:
        myargs.append(newarg)
    return tuple(myargs)

def fileArgs(file, mode, args):
    if args[0] == errno.EACCES and 'access' in dir(os):
        perms = ''
        permd = {'r': os.R_OK, 'w': os.W_OK, 'x': os.X_OK}
        pkeys = permd.keys()
        pkeys.sort()
        pkeys.reverse()
  
        for eachPerm in 'rwx':
            if os.access(file, permd[eachPerm]):
                perms += eachPerm
            else:
                perms += '-'

        if isinstance(args, IOError):
            myargs = []
            myargs.extend([arg for arg in args])
        else:
            myargs = list(args)

        myargs[1] = "'%s' %s (perms: '%s')" % (mode, myargs[1], perms)
        myargs.append(args.filename)

    else:
        myargs = args
    return tuple(myargs)

def myconnect(sock, host, port):
    try:
        sock.connect((host, connect))
    except socket.error as args:
        myargs = updArgs(args)
        if len(myargs) == 1:
            myargs = (errno.ENXIO, myargs[0])
        raise NetworkError(updArgs(myargs, host + ": " + str(port)))

def myopen(file, mode='r'):
    try:
        fo = open(file, mode)
    except IOError as args:
        raise FileError(fileArgs(file, mode, args))
    return fo

def testfile():
    """测试文件的异常"""
    file = TemporaryFile() # 生成临时文件 新建一个临时文件返回文件的引用和文件名
    f = open(file, 'w')
    f.close()

    for eachTest in ((0, 'r'), (0100, 'r'), (0400, 'w'), (0500, 'w')):
        try:
            os.chmod(file, eachTest[0])
            f = myopen(file, eachTest[1])
        except FileError as args:
            print("%s: %s" % (args.__class__.__name__, args))
    else:
        print(file, "opened ok ... perm ignored")

    os.chmod(file, 0777)
    os.unlink(file)

def testnet():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for eachHost in ('deli', 'www'):
        try:
            myconnect(s, 'deli', 8080)
        except NetworkError as args:
            print("%s: %s" % (args.__class__.__name__, args))

if __name__ == "__main__":
    testfile()
    testnet()
