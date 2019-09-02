#! /usr/bin/env python3

queue = []

def enQ():
    queue.append(input("Enter New String: ").strip())

def deQ():
    if len(queue) == 0:
        print("Cannot pop from an empty queue")
    else:
        print("Removed {}".format(queue.pop(0)))

def viewQ():
    print("queue = {}".format(queue))

CMDs = {"e": enQ, 'd': deQ, 'v': viewQ}

def showmenu():
    pr = """
(E)nqueue
(D)nqueue
(V)iew
(Q)uit
Enter choice: """
    while True:
        while True:
            try:
                choice = input(pr).strip().lower()
            except Exception as e:
                choice = "q"
            if choice not in "qdev":
                print("\nYou picked: [%s]" % choice)
            else:
                break
        if choice == "q":
            break
        CMDs[choice]()

if __name__ == "__main__":
    showmenu()
