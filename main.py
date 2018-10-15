## CISC 327 project main file

    
def inputLoop():
    end = False
    while (not end):
        action = input()
<<<<<<< HEAD
        if (action in transactions.keys()):
            transactions[action].execute(getState)
=======
>>>>>>> e29057b756a1fb94b7634019892e5d637a61ca60
        else:
            print("Invalid transaction")


            

inputLoop()
        
