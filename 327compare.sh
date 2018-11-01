#!/bin/bash
cd testCases/inputs
for i in *.txt
do
    echo "checking outputs of test $i"
    diff ../../SummaryFile/$i ../expected/$i
    #diff ../Outputs/$i.log ../expected/$i.log
done