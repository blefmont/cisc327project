'''
Manager
The manager is in charge of managing the transaction objects.
    It keeps data that the objects need to share (like user states)
    and insantiatates the objects.
'''
import sys
import transaction as tModule

fileName = sys.argv[1]
inf = open(fileName, "r")
        
transactions = {}
userState = ""
validServices = []
transactionSummary = []

## Returns the user state as a string. Will only return "loggedOut" "agent"
##  or planner. It can also raise a ValueError
def getState():
    global userState
    if (userState == "loggedOut" or userState == "agent" \
                or userState == "planner"):
        return userState
    else:
        raise ValueError("Impossible Error: userState uninitialized or invalid")

## Allows the transaction classes (used by Login and Logout) to change the
##  user state
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
        
## Needs to be run first, creates transaction objects and initalizes userState       
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
    transactions["changeticket"] = tModule.ChangeTicket()
