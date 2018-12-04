#!/bin/bash

cd dailyInputs
for i in *.txt
do
    echo "running test $i"
    cd ../Code
    py -3 main.py ../dailyInputs/$i
    mv "TransactionSummaryFile.txt" ../SummaryFile/$i

done

cd ../SummaryFile
rm MergeTransactionSummaryFile.txt
for i in *.txt
do
    cat $i >> MergeTransactionSummaryFile.txt
    echo "" >> MergeTransactionSummaryFile.txt
done

py -3 ../Code/backOffice.py MergeTransactionSummaryFile.txt ../centralservices.txt ../centralservices.txt ../validservices.txt
