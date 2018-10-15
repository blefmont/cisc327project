## CISC 327 project main file
import manager

    
def inputLoop():
    end = False
    while (not end):
        action = input()
        if (action in manager.transactions.keys()):
            manager.transactions[action].execute()
        else:
            print("Invalid transaction")


            

manager.initialize()
inputLoop()
        
