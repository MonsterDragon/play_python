#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

class User(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(11), User(13), User(15), User(2)]
print(sorted(users, key=lambda k: k.user_id))
