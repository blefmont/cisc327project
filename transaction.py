'''
    Transaction
'''

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

class SellTicket(Transaction):
    def __init__(self):
        super()

    def execute(self):
        self.serviceNumber = promptAndInput("Input Service Number:");
        self.serviceName = promptAndInput("Input Service Name:");
        

class Login(Transaction):
    def __init__(self):
        super()
    def execute(self, state):
        self.prompt("Login not yet implemented")




