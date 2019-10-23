#! /usr/bin/env python
# -*- coding:UTF-8 -*-

from socket import *

host = "127.0.0.1"
port = 21567
bufsize = 1024
addr = (host, port)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(addr)
    data = raw_input("> ")
    if not data:
        break
    tcpCliSock.send("%s\r\n" % data)
    data = tcpCliSock.recv(bufsize)
    if not data:
        break
    print data.strip()

