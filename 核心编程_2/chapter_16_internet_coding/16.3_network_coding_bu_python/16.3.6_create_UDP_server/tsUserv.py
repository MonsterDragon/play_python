#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from socket import *
from time import ctime

host = "0.0.0.0"
port = 21567
bufsize = 1024
addr = (host, port)

def udp_ser():
    udpservsock = socket(AF_INET, SOCK_DGRAM)
    udpservsock.bind(addr)

    while True:
        print("...waiting for message")
        data, addr = udpservsock.recvfrom(bufsize)
        udpservsock.sendto("[%s] %s" % (ctime(), data), addr)
        print("...received from and returned to: ", addr)

    udpservsock.close()

if __name__ == "__main__":

    udp_ser()

