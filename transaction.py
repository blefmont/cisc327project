'''
    Transaction
'''
import manager

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
    

    def checkValidNumber(self, name):
        pass

    def checkValidName(self, number):
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


