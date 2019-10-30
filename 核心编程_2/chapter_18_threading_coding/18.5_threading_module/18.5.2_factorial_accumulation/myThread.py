#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

import threading
from time import ctime

class MyThread(threading.Thread):

    def __init__(self, func, name="", *args):
        threading.Thread.__init__(self) # 调用父类的构造器
        self.func = func
        self.name = name
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print("starting ", self.name, " at: ", ctime())
        self.res = self.func(*self.args)
        print(self.name, " finished at: ", ctime())
