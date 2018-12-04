#!/bin/bash
## Weekly test script
## CISC 327 Assignment 6
## Michael Olson        20008033
## Brandon Christof     20014247

## Create the initial valid services file
printf '%s\r\n''00000' >validservices.txt
## Create the initial central services file
touch centralservices.txt

## For 5 times
for i in `seq 0 4`;
do
    for j in dailyInputs/*.txt;
    do
        rm ${j}
    done
    for j in dailyInputs/d${i}/*.txt;
    do
        mv ${j} ../${j}
    done
    ## Save the old VSF and CSF files
    cp validservices.txt vsfDay${i}.txt
    cp centralservices.txt csfDay${i}.txt
    ## Run the daily script
    ./327daily.sh
done 

## Save the final VSF and CSF files  
cp validservices.txt vsfFinal.txt
cp centralservices.txt csfFinal.txt
