# manager.py
# This file will manage things like valid transactions and user state.
import transaction as tModule

transactions = {}
userState = ""
validServices = []
transactionSummary = []

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
        validServices.clear()
        transactionSummary.clear()
        for i in transactions.values():
            i.newSession()
    else:
        if (type(st) != str): raise TypeError("State must be a string")
        else: raise ValueError('State must be "loggedOut, "agent" or "planner"')
        
        
def initialize():
    global userState
    global transactions
    userState = "loggedOut"

    transactions["login"] = tModule.Login()
    transactions["logout"] = tModule.Logout()
    transactions["createservice"] = tModule.CreateService()
    transactions["deleteservice"] = tModule.DeleteService()
    transactions["sellticket"] = tModule.SellTicket()
    transactions["cancelticket"] = tModule.CancelTicket()
