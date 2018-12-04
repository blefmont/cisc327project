'''
    Transaction
'''
#!/usr/bin/python
import sys
import math
import manager
import re

#Top level transaction class

class Transaction:
    
    def __init__(self):
        pass
    #To be called when a new session starts, allows objects to reset memory
    def newSession(self):
        pass
    
    #Execute attempts to complete the transaction 
    def execute(self):
        #by default checks if user is logged in
        if (manager.getState() == "loggedOut"):
            self.prompt("You must be logged in to perform that transaction")
            return False
        else:
            return True
    #To be used for the output to the user
    def prompt(self, s):
        print(s)    
    #Should handle all input for transaction classes
    def promptAndInput(self, s):
        self.prompt(s)
        response = manager.inf.readline()
        if (response[-1] == '\n'):
            response = response[0:-1]
        try:
            str(response)
        except TypeError:
            self.prompt("invalid input")
            #If there is an error trying to parse input, keep asking
            response = None
            while (response is None):
                response = self.promptAndInput(s)
        return response
    
    #Checks if a number follows proper format. Does not check valid services file
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
    #Check if service name follows proper format
    def checkValidName(self, n):
        try:
            # Regex, matches all strings that contain alphanumeric
            #   characters spaces and quote characters
            valid = "^[a-zA-Z0-9' ]*$";
            if type(n) != str:
                return False
            elif len(n) < 3 or len(n) > 39:
                return False       
            elif n[0] == " " or n[-1] == " ":
                return False       
            elif bool(re.match(valid, n)):
                return True
            else:
                return False
        except ValueError:
            return False
        
    ## Handels creating the lines for the transaction services.
    def createTSFLine(self, code, serviceNumber1 = "00000", amount = "0", \
                      serviceNumber2 = "00000", serviceName = "****", \
                      date = "0"):
        #Check that the code is valid
        if (not code in {'CAN', 'CHG', 'CRE', 'DEL', 'SEL', 'EOS'}):
            raise ValueError("Internal Error: The code given must be vailid")
        
        # Check that the service number is a valid entry
        if (not (serviceNumber1 == "00000" or self.checkValidNumber(serviceNumber1))):
            self.prompt("Invalid service number, transaction not completed")
            return False
        
        # Check that the ticket amount is valid
        amount = str(amount)
        if (amount.isnumeric()):
            if (not(int(amount) <= 1000 and int(amount) >= 0)):
                self.prompt("Ticket amount must be between 1 and 1000")
                return False
        else:
            self.prompt("Ticket amount is invalid")
            return False

        #Check that the second service number is valid
        if (not (serviceNumber2 == "00000" or self.checkValidNumber(serviceNumber2))):
            self.prompt("Invalid second service number, transaction not completed")
            return False
        
        #Check that the name is valid
        if (not (self.checkValidName(serviceName) or serviceName == "****")):
            self.prompt ("The service name is invalid, transaction not completed")
            return False

        #Check that the date is 0 or the code is CRE
        if (code == 'CRE' != date == "0"):
            self.prompt ("Date field had unexpected data, transaction not completed")
            return False        

        #Check that the line fits properly
        try:
            infoList = [code, serviceNumber1, amount, serviceNumber2, \
                         serviceName, date]
            infoList = [str(i) for i in infoList]
            line = " ".join(infoList)
        except (TypeError):
            return False

        if (len(line) > 68):
            self.prompt ("Error: the transaction has too many characters.")
            return False
        # Successful case
        else:
            if (code != 'EOS'):
                manager.transactionSummary.append(line + "\n")
                self.prompt ("Transaction successful")
                return True
            else:
                manager.transactionSummary.append(line)
                self.prompt ("Transaction successful")
                return True
'''
Class: Login
Handels logging in for the user, and reads the 
    valid services file into memory
'''
class Login(Transaction):
    
    def __init__(self):
        super()
        
    def execute(self):
        ## Reads in the valid services file
        try:
            VSFile = open("../validservices.txt")
            VSLines = VSFile.readlines()
            for line in VSLines:
                if (line.strip() == '00000'):
                    pass
                elif (not self.checkValidNumber(line)):
                    self.prompt("Valid services has unexpected content")
                    return None
            VSFile.close()
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
                for line in VSLines:
                    manager.validServices.append(line.strip())
            else:
                self.prompt("login failed, invalid mode")
                return None
                
        self.prompt("Login successful, welcome " + str(manager.getState()))
'''
Class: Logout
Transaction class that handels logging out, also reads the transaction summary
into file.
'''
class Logout(Transaction):
    def __init__(self):
        super()
    def execute(self):
        if (not super().execute()):
            return None
        try:
            TSF = open("TransactionSummaryFile.txt", 'wt')
            if (self.createTSFLine('EOS')):
                TSF.writelines(manager.transactionSummary)
            else:
                self.prompt("Error while creating TSF")
                return None
            TSF.close()
        except IOError:
            self.prompt("IO error during logout")
            return None
        manager.changeState("loggedOut")
'''
Class CreateService
Transaction class that handels createservice transaction.
Also deals with confirming that dates are in the proper format
'''
class CreateService(Transaction):
    def __init__(self):
        super()
    def execute(self):
        if (not super().execute()):
            return None
        if (manager.getState() != "planner"):
            self.prompt("You must be in planner mode to use create service")
            return None
        
        snum = self.promptAndInput("Please enter the service number")
        date = self.promptAndInput("Please enter the service date in format YYYYMMDD")
        sname = self.promptAndInput("Please enter the service name")
        
        if (not self.checkValidNumber(snum)):
            self.prompt("Invalid service number")
            return None
        elif ((not self.checkValidName(sname)) or sname.count("'")):
            self.prompt("Invalid service name")
            return None
        elif (not self.checkValidDate(date)):
            self.prompt("Invalid service date")
            return None
        elif (manager.validServices.count(snum)):
            self.prompt("Services number already exists")
            return None
        else:
            self.createTSFLine('CRE', serviceNumber1 = snum, serviceName = sname, date = date)
            
    def checkValidDate(self, date):
        
            stdate = str(date)
            if (not stdate.isnumeric()):
                return False
            if (len(stdate) != 8):
                return False
            if (not(int(stdate[0:4]) >= 1980 and int(stdate[0:4]) <= 2999)):
                return False
            if (not(int(stdate[4:6]) >= 1 and int(stdate[4:6]) <= 12)):
                return False
            if (not(int(stdate[6:8]) >= 1 and int(stdate[6:8]) <= 31)):
                return False
            return True
'''
Class DeleteService
transaction class that handels deleting a service and taking it away
from the valid services memory so no further tranasactions can be performed
'''
class DeleteService(Transaction):
    def __init__(self):
        super()
    def execute(self):
        if (not super().execute()):
            return None
        if (manager.getState() != "planner"):
            self.prompt("You must be in planner mode to execute this transaction")
            return None
        
        snum = self.promptAndInput("What is the service number?")
        sname = self.promptAndInput("What is the service name?")
        if (not self.checkValidNumber(snum)):
            self.prompt("Invalid service number")
            return None
        if (not self.checkValidName(sname)):
            self.prompt("Invalid service name")
            return None
        if (not manager.validServices.count(snum)):
            self.prompt("Service number does not exist")
            return None
        else:
            manager.validServices.remove(snum)
            self.createTSFLine('DEL', serviceNumber1 = snum, serviceName = sname)
        
class SellTicket(Transaction):
    def __init__(self):
        super()

    def execute(self):
        if (not super().execute()):
            return None
        sNum = self.promptAndInput("Input Service Number:")
        ticketAmount = self.promptAndInput("Input Amount of Tickets")
        
        if (not self.checkValidNumber(sNum)):
            self.prompt("Invalid service number")
            return None
        if (not manager.validServices.count(sNum)):
            self.prompt("Service number does not exist")
            return None
        self.createTSFLine('SEL', serviceNumber1 = sNum, amount = ticketAmount)
        
class CancelTicket(Transaction):
    def __init__(self):
        self.transactionHistory = {}
    def newSession(self):
        self.transactionHistory.clear()
    def execute(self):
        if (not super().execute()):
            return None

        sNum = self.promptAndInput("Input Service Number:")
        ticketAmount = self.promptAndInput("Input Amount of Tickets")
        
        if (not self.checkValidNumber(sNum)):
            self.prompt("Invalid service number")
            return None
        if (not manager.validServices.count(sNum)):
            self.prompt("Service number does not exist")
            return None
        if (not ticketAmount.isnumeric()):
            self.prompt("Invalid ticket amount")
            return None
        if (manager.getState() == "agent"):
            if (sNum in self.transactionHistory.keys()):
                self.transactionHistory[sNum] += int(ticketAmount)
            else:
                self.transactionHistory[sNum] = int(ticketAmount)
            if (self.transactionHistory[sNum] > 10):
                self.prompt("Can not perform more than 10 of these transactions on one service")
                return None
            if (sum(self.transactionHistory.values()) > 20):
                self.prompt("Can not perform more than 20 change tickets in agent mode.")
                return None
        self.createTSFLine('CAN', serviceNumber1 = sNum, amount = ticketAmount)           
        
class ChangeTicket(Transaction):
    def __init__(self):
        super()
        self.numOfTransactions = 0
    def newSession(self):
        self.numOfTransactions = 0
    def execute(self):
        if (not super().execute()):
            return None
        
        sNumOne = self.promptAndInput("Input current service number")
        sNumTwo = self.promptAndInput("Input destination service number")
        ticketAmount = self.promptAndInput("Input number of tickets to change")

        if (not (self.checkValidNumber(sNumOne) and self.checkValidNumber(sNumTwo))):
            self.prompt("Invalid service number")
            return None
        if (not (manager.validServices.count(sNumOne) and manager.validServices.count(sNumTwo))):
            self.prompt("Service number does not exist")
            return None
        if (not ticketAmount.isnumeric()):
            self.prompt("Invalid ticket amount")
            return None
        
        if (manager.getState() == "agent"):
            self.numOfTransactions += int(ticketAmount)
            if (self.numOfTransactions > 20):
                self.prompt("Too many transactions for this mode")
                return None
        self.createTSFLine("CHG", serviceNumber1 = sNumOne, serviceNumber2 = sNumTwo, amount = ticketAmount)




