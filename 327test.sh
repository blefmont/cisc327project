#!/bin/bash                                                                    

cd testCases/inputs
for i in *.txt                                                                 
do                                                                             
    echo "running test $i"
    cd ../../Code
    #echo $PWD
    python3 main.py ../testCases/inputs/$i
    cp "TransactionSummaryFile.txt" ../Outputs/$i.log
    mv "TransactionSummaryFile.txt" ../SummaryFile/$i
    
done