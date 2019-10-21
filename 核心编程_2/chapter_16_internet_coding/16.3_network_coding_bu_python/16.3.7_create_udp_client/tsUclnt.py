#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from socket import *

host = "106.13.136.202"
port = 21567
bufsize = 1024
addr = (host, port)

def udp_client():
    udpclisock = socket(AF_INET, SOCK_DGRAM)

    while True:
        data = input("> ")
        if not data:
            break
        udpclisock.sendto(data, addr)
        data, addr = udpclisock.recvfrom(bufsize)
        if not data:
            break
    udpclisock.close()

if __name__ == "__main__":

    udp_client()
