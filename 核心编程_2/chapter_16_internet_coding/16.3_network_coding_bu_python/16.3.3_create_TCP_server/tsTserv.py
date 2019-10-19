#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from socket import *
from time import ctime

class Serv_socket(object):
    """TCP服务器"""
    def __init__(self, host, port, bufsize, conn_num):
        self.host = host
        self.port = port
        self.bufsize = bufsize
        self.conn_num = conn_num

    def init_socket(self):
        tcp_socket = socket(AF_INET, SOCK_STREAM)
        addr = (self.host, self.port)
        tcp_socket.bind(addr)
        tcp_socket.listen(self.conn_num)
        return tcp_socket

    def serv_loop(self, socket_obj):
        while True:
            print("waiting for connection")
            tcpcli, addr = socket_obj.accept()
            print("connected from: ", addr)
            while True:
                data = tcpcli.recv(self.bufsize)
                print("recieve data is %s" % data)
                if not data:
                    break
                tcpcli.send("[%s] %s" % (ctime, data))
                tcpcli.close()

    def main(self):
        create_socket = self.init_socket()
        self.serv_loop(create_socket)

if __name__ == "__main__":
    serv_ins = Serv_socket("127.0.0.1", 21567, 1024, 100)
    serv_ins.main()
