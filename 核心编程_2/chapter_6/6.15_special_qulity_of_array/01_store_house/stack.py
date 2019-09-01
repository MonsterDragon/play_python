#! /usr/bin/env python3

"""
堆栈是一个后进先出的数据结构。push代表把一个对象添加到堆栈中。繁殖要拿出一个对象，则是pop
"""

stack = []

def pushit():
    stack.append(input("Enter New String:")) # string()默认移除字符串首尾的空白字符

def popit():
    if len(stack) == 0:
       print("Cannot pop from any empty stack")
    else:
       # print("Removed [', `stack.pop()`, ']")
       print("Removed [', {}, ']".format(stack.pop()))

def viewstack():
    print(stack)

CMDs = {"u": pushit, "o": popit, "v": viewstack}

def showmenu():
    pr = """
p(U)sh
p(O)p
(V)iew
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
            if choice not in "uvoq":
                print("Invalid option, try again")
            else:
                break
        if choice == "q":
            break
        CMDs[choice]()

if __name__ == "__main__":

    showmenu()
