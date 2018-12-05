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
                        int(sLine[2]), int(sLine[3]),\
                        ' '.join(sLine[4:-1]))
        transactions.append(t)
    return transactions

def readOCSF(oCSFcontents):
    services = []
    for line in oCSFcontents:
        sLine = line.split()
        if (len(sLine) >= 4):
            s = Service(int(sLine[0]), int(sLine[2]), ' '.join(sLine[3:len(sLine)]))
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
                if (s.ticketsSold + t.amount <= s.capacity):
                    s.ticketsSold += t.amount
                else:
                    print("Sell ticket transaction for {} ignored because at capacity".format(t.snum1))
            else:
                print("Sell ticket transaction for {} ignored because of invalid service".format(t.snum1))                
        if (t.tType == 'CHG'):
            s1 = findService(services, t.snum1)
            s2 = findService(services, t.snum2)
            if (s1 and s2):
                if (s1.ticketsSold - t.amount >= 0 and s2.ticketsSold + t.amount <= s2.capacity):
                    s1.ticketsSold -= t.amount
                    s2.ticketsSold += t.amount
                else:
                    print("Change ticket transaction for {} ignored because one of the services is full or empty".format(t.snum1))
            else:
                print("Change ticket transaction for {} ignored because of invalid service".format(t.snum1))  
        if (t.tType == 'CAN'):
            s = findService(services, t.snum1)
            if (s):
                if (s.ticketsSold - t.amount >= 0):
                    s.ticketsSold -= t.amount
                else:
                    print("Cancel ticket transaction for {} ignored because no tickets are sold".format(t.snum1))
            else:
                print("Cancel ticket transaction for {} ignored because of invalid service".format(t.snum1))  

    
    services.sort(key=lambda s : s.number)
    vsfContents = []
    nCSFcontents = []
    for s in services:
        vsfContents.append(str(s.number) + '\n')
        nCSFcontents.append(" ".join((str(s.number), str(s.capacity), str(s.ticketsSold),\
                                      s.name, '\n')))
    vsfContents.append('00000')

    return nCSFcontents, vsfContents
def findService(services, sNum):
    for s in services:
        if (s.number == sNum):
            return s
    return None
