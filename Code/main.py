## CISC 327 project main file
## Authors: Michael Olson 20008033
##          Brandon Christof 20014247

import sys
import manager

## Input loop is what handels the input from the user in between transactions
def inputLoop():
    end = False
    while (not end):
        action = manager.inf.readline().strip()
        if (action in manager.transactions.keys()):
            manager.transactions[action].execute()
        elif (action == "debug"):
            break
        elif (not action):
            break
        else:
            print("Invalid transaction")

            

manager.initialize()
inputLoop()
        
