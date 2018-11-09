'''
Back office functions
'''
## Objects for storing the data
class Transaction():
    def __init__(self, tType, snum1, amount, snum2, name):
        self.tType = tType
        self.snum1 = snum1
        self.amount = amount
        self.snum2 = snum2
        self.name = name
                    
class Service():
    def __init__(self, number, ticketsSold, name, capacity = 30):
        self.number = number
        self.ticketsSold = ticketsSold
        self.name = name
        self.capacity = capacity

def readMTSF(mTSFcontents):
    transactions = []
    for line in mTSFcontents:
        sLine = line.split()
        t = Transaction(sLine[0], int(sLine[1]), \
                        int(sLine[2]), int(sline[3]),\
                        ' '.join(sLine[4:-1]))
        transaction.append(t)
    return transactions

def readOCSF(oCSFcontents):
    services = []
    for line in oCSFcontents:
        sLine = line.split()
        s = Service(int(sLint[0]), int(sLine[2]), sLine[3])
        services.append(s)
    return services

def applyTransactions(transactions, services):
    
    ## Loop through the transactions, applying changes
    for t in transactions:
        if (t.tType == 'CRE'):
            serviceExists = findService(services, t.snum1)
            if (not serviceExists):
                s = Service(t.snum1, 0, t.name)
                services.append(s)
            else:
                print("Create service transaction ignored because service {} already exists".format(t.snum1))
                
        if (t.tType == 'DEL'):
            s = findService(services, t.snum1)
            if (s):
                services.remove(s)
            else:
                print("Delete service transaction ignored because service {} does not exist".format(t.snum1))

        if (t.tType == 'SEL'):
            s = findService(services, t.snum1)
            if (s):
                if (s.ticketsSold + 1 <= s.capacity):
                    s.ticketsSols += 1
                else:
                    print("Sell ticket transaction for {} ignored because at capacity".format(t.snum1))
            else:
                print("Sell ticket transaction for {} ignored because of invalid service".format(t.snum1))                
        if (t.tType == 'CHG'):
            s1 = findService(services, t.snum1)
            s2 = findService(services, t.snum2)
            if (s1 and s2):
                if (s1.ticketsSold - 1 >= 0 and s2.ticketsSold + 1 <= s2.capacity):
                    s1.ticketsSols -= 1
                    s2.ticketsSols += 1
                else:
                    print("Change ticket transaction for {} ignored because one of the services is full or empty".format(t.snum1))
            else:
                print("Change ticket transaction for {} ignored because of invalid service".format(t.snum1))  
        if (t.tType == 'CAN'):
            s = findService(services, t.snum1)
            if (s):
                if (s.ticketsSold - 1 >= 0):
                    s.ticketsSols -= 1
                else:
                    print("Cancel ticket transaction for {} ignored because no tickets are sold".format(t.snum1))
            else:
                print("Cancel ticket transaction for {} ignored because of invalid service".format(t.snum1))  
    ## 
def findService(services, sNum):
    for s in service:
        if (s.number == sNum):
            return s
    return None
