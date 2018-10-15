'''
    Transaction
'''

import math
import manager
import re

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

    def checkValidName(self, n):
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
        
    def checkValidDate(self, date):
        try:
            stdate = str(date)
            if (not stdate.isnumeric()):
                return None
            if (len(stdate) != 8):
                return None
            if (not(int(stdate[0:4]) >= 1980 and int(stdate[0:4] <= 2999))):
                return None
            if (not(int(stdate[4:6]) >= 1 and int(stdate[4:6] <= 12))):
                return None
            if (not(int(stdate[6:8]) >= 1 and int(stdate[6:8] <= 31))):
                return None
            return True
        
        except BaseException:
            return None

            
    def createTSFLine(self, code, serviceNumber1 = "00000", amount = "0", \
                      serviceNumber2 = "00000", serviceName = "****", \
                      date = "0"):
        #Check that the code is valid
        if (not code in {'CAN', 'CHG', 'CRE', 'DEL', 'SEL', 'EOS'}):
            raise ValueError("Internal Error: The code given must be vailid")
        
        # Check that the service number is a valid entry
        if (not (serviceNumber1 == "00000" or self.checkValidNumber(serviceNumber1))):
            self.prompt("Invalid service number, transaction not completed")
            return None
        
        # Check that the ticket amount is valid
        amount = str(amount)
        if (amount.isnumeric()):
            if (not(int(amount) <= 1000 and int(amount) >= 0)):
                self.prompt("Ticket amount must be between 1 and 1000")
                return None
        else:
            self.prompt("Ticket amount is invalid")
            return None

        #Check that the second service number is valid
        if (not (serviceNumber2 == "00000" or self.checkValidNumber(serviceNumber2))):
            self.prompt("Invalid second service number, transaction not completed")
            return None
        
        #Check that the name is valid
        if (not (self.checkValidName(serviceName) or serviceName == "****")):
            self.prompt ("The service name is invalid, transaction not completed")
            return None

        #Check that the date is 0 or the code is CRE
        if (code == 'CRE' != date == "0"):
            self.prompt ("Date field had unexpected data, transaction not completed")
            return None
        try:
            infoList = [code, serviceNumber1, amount, serviceNumber2, \
                         serviceName, date]
            infoList = [str(i) for i in infoList]
            line = " ".join(infoList)
        except (TypeError):
            return None

        if (len(line) > 68):
            self.prompt ("Error: the transaction has too many characters.")
            return None
        
        else:
            manager.transactionSummary.append(line)
            self.prompt ("Transaction successful")
            
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
                
        self.prompt("Login successful, welcome " + str(manager.getState()))



        

