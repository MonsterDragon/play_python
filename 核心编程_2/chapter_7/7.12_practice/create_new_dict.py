#! /usr/bin/env python3
# -*- encode=utf-8 -*-

dict_o = {"a": 12, "b": 13, 1: "cd"}

def main():
    key_tuple = tuple(dict_o.keys())
    print(key_tuple)
    value_tuple = tuple(dict_o.values())
    print(value_tuple)
    new_dict = dict(zip(value_tuple, key_tuple))
    print(new_dict)

if __name__ == "__main__":
    main()
