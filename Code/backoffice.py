'''
Back Office
Inputs:
    Merged Transaction Summary File
    Old Central Services File
Outputs:
    Standard output log
    New Central Services File
    Valid Services File
    
Authors:
    Michael Olson      20008033
    Brandon Christof   20014247
'''

import sys
from backofficefunctions import *

if (len(sys.argv) > 1):
    mergedTSFfname =    sys.argv[1]
    oldCSFfname =       sys.argv[2]
    newCSFfname =       sys.argv[3]
    VSFfname =          sys.argv[4]
else:
    

## Read in the merged TSF
mTSF = open(mergedTSFfname)
mTSFcontents = mTSF.readlines()
transactions = readMTSF(mTSFcontents)
mTSF.close()

## Read in the old central services file
oCSF = open(oldCSFfname)
oCSFcontents = oCSF.readlines()
services = readOCSF(oCSFcontents)
oCSF.close()

## Apply the transactions

nCSFcontents, VSFcontents = applyTransactions()

## Write the new central services file
nCSF = open(newCSFfname, 'w')
nCSF.writelines(nCSFcontents)
nCSF.close()

## Write the new Valid Services file
vsf = open(VSFfname, 'w')
vsf.writelines(VSFcontents)
vsf.close()
