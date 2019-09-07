#! /usr/bin/env python3
# -*- encode=utf-8 -*-
import string

dict_o = {}

def enter_dict():
    str_enter = "Please enter the key: "
    letters = string.ascii_letters
    while True:
        dict_key = input(str_enter)
        if dict_key in dict_o:
            str_enter = "key token, try another: "
            continue
        elif dict_key[0].lower() not in letters:
            str_enter = "Invalid string, try another: "
        else:
            break
    dict_value = input("Please enter the value: ")
    dict_o[dict_key] = dict_value

def roll_dict():
    key_list = list(dict_o.keys())
    key_list.sort(reverse = False)
    print("The keys list is {}".format(key_list))
    print([(i, dict_o[i]) for i in key_list])

menu = {'e': enter_dict, 'r': roll_dict}

def main():
    promot = """
(E)nter
(R)oll
(Q)uit
"""
    done = True
    while done:
        chosen = True
        while chosen:
            try:
                choice = input(promot).strip()[0].lower()
            except Exception as e:
                choice = 'q'
            if choice not in "erq":
                print("invalid option, try again")
            else:
                print("Your chose is {}".format(choice))
                chosen = False
        if choice == 'q':
            done = False
        else:
            menu[choice]()

if __name__ == "__main__":
    main()
    # roll_dict()
