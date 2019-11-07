#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from operator import itemgetter

rows = [
        {'fname': 'Brain', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
        ]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
rows_lambda_fname = sorted(rows, key=lambda k: k['fname'])
rows_lambda_uid = sorted(rows, key=lambda k: k['uid'])
print(rows_lambda_fname)
print(rows_lambda_uid)
print(min(rows, key=lambda k: k['uid']))
print(max(rows, key=lambda k: k['uid']))
