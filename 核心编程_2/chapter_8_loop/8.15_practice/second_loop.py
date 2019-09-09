#! /usr/bin/env python3
# -*- encode=utf-8 -*-

def from_fun():
    int_1 = input("Please enter your start num: ")
    while not int(int_1):
        int_1 = input("Invalid enetr arags, try again: ")
    return int_1

def to_fun():
    int_2 = input("Please enter your end num: ")
    while not int(int_2):
        int_2 = input("Invalid enetr arags, try again: ")
    return int_2

def incre_fun():
    start_int = from_fun()
    end_int = to_fun()
    int_3 = input("Please enter your step num: ")
    while not int(int_3):
        int_3 = input("Invalid enetr arags, try again: ")
    for i in range(int(start_int), int(end_int), int(int_3)):
        print("{}, "format(i), end="")

dict_o = {"i": incre_fun}

def main():
    pr = """
(i)ncrement
(q)uit
"""
    chosen = True
    while chosen:
        done = True
        while done:
            try:
                choice = input(pr).strip()[0].lower()
            except Exception as e:
                print("Invalid arags, try again")
            if choice in 'iq':
                done = False
        if choice == 'q':
            chosen = False
        else:
            dict_o[choice]()

if __name__ == "__main__":
    main()
