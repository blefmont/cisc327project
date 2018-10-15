## CISC 327 project main file
from transaction import *

transactions = {}
__userState__ = ""

def getState():
    if (__userState__ == "loggedOut" or __userState__ == "agent" \
                or userState == "planner"):
        return __userState__
    else:
        raise ValueError("Impossible Error: userState uninitialized or invalid")

def changeState(newState):
    if (newState == "loggedOut" or newState == "agent" \
                or newState == "planner"):
        __userState__ = newState
    else:
        if (type(st) != str): raise TypeError("State must be a string")
        else: raise ValueError('State must be "loggedOut, "agent" or "planner"')
        
        
def initialize():
    __userState__ = "loggedOut"
    login = Login()
    transactions["login"] = login
def inputLoop():
    end = False
    while (not end):
        action = input()
        if (action in transactions.keys()):
            transactions[action].execute()
        else:
            print("Invalid transaction")


initialize()
inputLoop()
        
