#! /usr/bin/env python3
# -*- coding=UTF-8 -*-

import sys

class MyOpen(object):
    
    def __init__(self, file_name):
        """初始化方法"""
        self.file_name = file_name
        self.file_handler = None
        return 

    def __enter__(self):
        """enter方法，返回file_handler"""
        print("enter:", self.file_name)
        self.file_handler = open(self.file_name, 'r')
        return self.file_handler

    def __exit__(self, exc_type, exc_val, exc_tb):
        """exit方法，关闭文件并返回True"""
        print("exit:", exc_type, exc_val, exc_tb)
        if self.file_handler:
            self.file_handler.close()
        return False

def main(args):
    with MyOpen(args) as f:
        for line in f:
            try:
                print(float(line))
            except Exception as e:
                print(e)

if __name__ == "__main__":
    main(sys.argv[1])
