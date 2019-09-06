#! /usr/bin/env python3
# -*- encode=utf-8 -*-

db = {}

def newuser():
    login = "login desired: "
    while True:
        name = input(login)
        if name in db:
            login = "name taken, try another"
        else:
            break
    pwd = input("passwd: ")
    db[name] = pwd

def olduser():
    name = input("login: ")
    pwd = input("passwd: ")
    passwd = db.get(name)
    if passwd == pwd:
        print("welcome back")
    else:
        print("login incorrect")

opp = {'n': newuser, 'e': olduser}

def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
"""
    done = False
    while not False:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except Exception as e:
                choice = 'q'
                print("Your picked is %s" % choice)
            if choice not in "neq":
                print("invalid option, try again")
            else:
                chosen = True
        if choice == 'q':
            done = True
        opp[choice]()

if __name__ == "__main__":
    showmenu()
