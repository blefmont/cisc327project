'''
Back office functions
'''
class Transaction():
    def __init__(self, tType, snum1, ticketAmount, snum2, name):
        self.tType = tType
        self.snum1 = snum1
        self.ticketAmount = ticketAmount
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
        transaction.append(Transaction(sLine[0], int(sLine[1]), \
                                       int(sLine[2]), int(sline[3]),\
                                       ' '.join(sLine[4:-1])))
    return transactions

def readoCSF()
        
