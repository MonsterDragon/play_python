#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import ftplib
import os
import socket

host = "ftp.mozilla.org"
dirn = "pub/mozilla.org/webtools"
file_name = "bugzilla-Latest.tar.gz"

def main():
    try:
        f = ftplib.FTP(host)
    except (socket.error, socket.gaierror), e:
        print "ERROR: cannot reach \"%s\"" % host
        return
    print "***Connected to host \"%s\"" % host

    try:
        f.login()
    except ftplib.error_perm:
        print "ERROR: cannot login anonymously"
        f.quit()
        return
    print "*** Logged in as \"annoymous\""

    try:
        f.cwd(dirn) # 把当前工作目录设置配path
    except ftplib.error_perm:
        print "ERROR: cannot CD to \"%s\"" % dirn
        f.quit()
        return
    print "*** Changed to \"%s\" folder" % dirn

    try:
        f.retrbinary("RETR %s" % file_name, open(file_name, 'wb').write) # 下载
    except ftplib.error_perm:
        print "ERROR: cannot read file \"%s\" to CWD" % file_name
        os.unlink(file_name)
    else:
        print "*** Downloaded \"%s\" to CWD" % file_name
    f.quit()
    return

if __name__ == "__main__":
    main()
