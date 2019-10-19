#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

import re
from socket import *

class Cli_socket(object):
    def __init__(self, host, port, bufsize):
        self.host = host
        self.port = eval(port)
        self.bufsize = eval(bufsize)

    def create_sock(self):
        cli_sock = socket(AF_INET, SOCK_STREAM)
        addr = (self.host, self.port)
        print(addr)
        cli_sock.connect(addr)
        return cli_sock

    def sock_loop(self, sock_obj):
        while True:
            data = input("> ")
            if not data:
                break
            sock_obj.send(data.encode())
            data = sock_obj.recv(self.bufsize)
            real_data = data.decode()
            print("type:", type(data))
            if not data:
                break
            sea_obj = re.search(r"(\[.+\]) b\'(.+)\'", real_data).group(2)
            print(sea_obj, type(sea_obj))
            regex_hex_string = r"(\\x.{2})+"
            regex_hex_element = r"\\x(.{2})"
            a = lambda m:bytes.fromhex(re.sub(regex_hex_element, r'\1', m))
            print(a(sea_obj))
            result = re.sub(regex_hex_string, lambda m:
                    bytes.fromhex(re.sub(regex_hex_element, r'\1',
                        m.group(0))).decode('utf-8'), sea_obj)
            print(result)
        sock_obj.close()

    def main(self):
        sock_obj = self.create_sock()
        self.sock_loop(sock_obj)

if __name__ == "__main__":
    cli_ins = Cli_socket("127.0.0.1", "21567", "1024")
    cli_ins.main()
