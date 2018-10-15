# manager.py
# This file will manage things like valid transactions and user state.
import transaction as tModule

transactions = {}
userState = ""

def getState():
    global userState
    if (userState == "loggedOut" or userState == "agent" \
                or userState == "planner"):
        return userState
    else:
        raise ValueError("Impossible Error: userState uninitialized or invalid")

def changeState(newState):
    global userState
    if (newState == "loggedOut" or newState == "agent" \
                or newState == "planner"):
        userState = newState
    else:
        if (type(st) != str): raise TypeError("State must be a string")
        else: raise ValueError('State must be "loggedOut, "agent" or "planner"')
        
        
def initialize():
    global userState
    global transactions
    userState = "loggedOut"
    login = tModule.Login()
    transactions["login"] = login
