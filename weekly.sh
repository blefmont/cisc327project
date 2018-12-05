#!/bin/bash
## Weekly test script
## CISC 327 Assignment 6
## Michael Olson        20008033
## Brandon Christof     20014247

## Create the initial valid services file
echo '00000' >validservices.txt
## Create the initial central services file
echo '' >centralservices.txt

## For 5 times
for i in `seq 1 5`;
do
    for existingFile in dailyInputs/*.txt;
    do
        rm ${existingFile}
    done
    cp SummaryFile/MergeTransactionSummaryFile.txt Outputs/MTSFd${i}.txt
    for existingFile in SummaryFile/*txt;
    do
        rm ${existingFile}
    done
    for iFile in dailyInputs/d${i}/*.txt;
    do
        cp ${iFile} dailyInputs/$(basename $iFile)
    done
    ## Save the old VSF and CSF files
    cp validservices.txt vsfPreDay${i}.txt
    cp centralservices.txt csfPreDay${i}.txt
    ## Run the daily script
    ./327daily.sh
done 

## Save the final VSF and CSF files  
cp validservices.txt vsfFinal.txt
cp centralservices.txt csfFinal.txt
