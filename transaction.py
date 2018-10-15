'''
    Transaction
'''
<<<<<<< HEAD

import math
=======
import manager
>>>>>>> e29057b756a1fb94b7634019892e5d637a61ca60

class Transaction:
    
    def __init__(self):
        pass

    def execute(self):
        self.prompt("execute not implemented yet")

    def prompt(self, s):
        print(s)
        pass    

    def promptAndInput(self, s):
        self.prompt("promptAndInput not yet implemented")
        return s
    

    def checkValidNumber(self, number):
        try:
            if int(str(n)[:1]) == 0:
                return False
            x = int(n);
            if x > 10000 and x < 99999:
                return True
            else:
                return False
        except ValueError:
            return False

    def checkValidName(self, name):
        pass        

    def createTSFLine(self, code, serviceNumber1 = "00000", amount = "0", \
                      serviceNumber2 = "00000", serviceName = "****", \
                      date = "0"):
        pass

class Login(Transaction):
    def __init__(self):
        super()
    def execute(self):
        state = manager.getState()
        if (state != "loggedOut"):
            self.prompt("Incorrect state")
        else:
            self.prompt("correct state")
        self.prompt("Login not yet implemented")


<<<<<<< HEAD
        

=======
>>>>>>> e29057b756a1fb94b7634019892e5d637a61ca60
