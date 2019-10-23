#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

import re
from socket import *

host = "localhost"
port = 21567
bufsize = 1024
addr = (host, port)

def udp_client(addr):
    udpclisock = socket(AF_INET, SOCK_DGRAM)

    while True:
        data = input("> ")
        if not data:
            break
        regex_hex_string = r"(\\x.{2})+"
        regex_hex_element = r"\\x(.{2})"
        udpclisock.sendto(data.encode(), addr)
        real_data, addr = udpclisock.recvfrom(bufsize)
        print("real_data: ", real_data)
        try:
            re.search(r"\[\'.+\'\] (.+)", str(real_data)).group(1)
        except Exception as e:
            print(real_data, addr)
        else:
            sea_obj = re.search(r"(\[\'.+\'\] (.+))", real_data.decode()).group(2)
            print("sea_obj: ", sea_obj)
            # a = lambda m:bytes.fromhex(re.sub(regex_hex_element, r'\1', m))
            # print(a(sea_obj))
            result = re.sub(regex_hex_string, lambda m:
                    bytes.fromhex(re.sub(regex_hex_element, r'\1',
                        m.group(0))).decode('utf-8'), sea_obj)
            print(result, addr)
        if not data:
            break
    udpclisock.close()

if __name__ == "__main__":

    udp_client(addr)
