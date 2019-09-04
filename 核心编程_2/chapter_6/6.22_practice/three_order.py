#! /usr/bin/env python3
# -*- encoding=utf-8 -*-

def input_fun():
    num_str = input("please input nums: ")
    num_list = []
    for i in range(len(num_str)):
        try:
            num = int(num_str[i])
            print(num)
            num_list.append(num)
            print(num_list)
            if i == len(num_str)-1:
                print(num_list.sort(reverse=True))
        except Exception as e:
            print("Value Error")
            return 1
    num_list.sort(reverse=True)
    print(num_list)

CMDs = {"e": input_fun}

def main():
    pr = """
(E)nter
(Q)uit
Enter choice:
"""
    while True:
        while True:
            try:
                choice = input(pr).strip()[0].lower()
            except Exception as e:
                choice = "q"

            print("\nYou picked: [%s]" % choice)
            if choice not in "eq":
                print("Invalid option, try again")
            else:
                break
        if choice == "q":
            break
        CMDs[choice]()

if __name__ == "__main__":
    main()
