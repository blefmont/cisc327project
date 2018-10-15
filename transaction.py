'''
    Transaction
'''

import math
import manager

class Transaction:
    
    def __init__(self):
        pass

    def execute(self):
        self.prompt("execute not implemented yet")

    def prompt(self, s):
        print(s)    

    def promptAndInput(self, s):
        response = input(s)
        try:
            str(response)
        except TypeError:
            self.prompt("invalid input")
            response = None
            while (response is None):
                response = self.promptAndInput(s)
        return response
    

    def checkValidNumber(self, n):
        try:
            if int(str(n)[:1]) == 0:
                return False
            x = int(n);
            if x >= 10000 and x <= 99999:
                return True
            else:
                return False
        except ValueError:
            return False

    def checkValidName(self, name):
        try:
            valid = "^[a-zA-Z0-9' ]*$";
            if type(n) != str:
                return False
            elif len(n) < 3 or len(n) > 39:
                return False       
            elif n[:1] == " " or n[-1:] == " ":
                return False       
            elif bool(re.match(valid, n)):
                return True
            else:
                return False
        except ValueError:
            return False     

    def createTSFLine(self, code, serviceNumber1 = "00000", amount = "0", \
                      serviceNumber2 = "00000", serviceName = "****", \
                      date = "0"):
        pass

class Login(Transaction):
    
    def __init__(self):
        super()
        
    def execute(self):
        ## Reads in the valid services file
        try:
            VSFile = open("validServices.txt")
            VSLines = VSFile.readlines()
            for line in VSLines:
                if (self.checkValidNumber(line.strip())):
                    manager.validServices.append(line.strip())
                else:
                    self.prompt("Valid services has unexpected content")
                    return None
        except IOError:
            self.prompt("Error reading valid services file")
            return None
        
        ## Changes the state of the user
        state = manager.getState()
        if (state != "loggedOut"):
            self.prompt("Can not login unless logged out")
            return None
        else:
            response = self.promptAndInput("What mode would you like to enter? Options are agent or planner.")
            if (response == "agent" or response == "planner"):
                manager.changeState(response)
            else:
                self.prompt("login failed, invalid mode")
                return None
        
        
                
        self.prompt("Login not yet fully implemented")



        

