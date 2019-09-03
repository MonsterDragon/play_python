#! /usr/bin/env python3
# -*- encoding=utf-8 -*-

def input():
    num_str = input("please input nums: ")
    num_list = []
    for i in range(len(num_str)):
        try:
            num = int(num_str[i])
        except Exception as e:
            print("Value Error")
            return 1
        num_list.append(num)
    print(num_list.sort(reverse=True))

CMDs = {"e": "input"}

# def showmenu():
#     pr = """
#     (E)nter
#     (Q)uit
# Enter Choice:"""
#     return pr

def main():
    #showmenu()
    pr="""
(E)nter
(Q)uit
Enter Choice:"""
    while True:
        while True:
            try:
                choice = input(pr).strip()[0].lower()
            except Exception as e:
                choice = 'q'
            if choice not in "eq":
                print("Invalid option, try again")
            else:
                break
        if choice == 'q':
            break
        CMDs['choice']()

if __name__ == "__main__":
    main()
