#-*- coding: utf-8 -*-
import os

data_src = "/Users/ghostchef/data/shcool-card-data/"

for index in range(1, 10):
    inputFileName = data_src + "original-logs/ykt_his_trade_20140" +str(index)+".txt"
    outputFileName = data_src + "cleantest/cleaned_20140"+ str(index) + ".txt"
    inputFile = open(inputFileName, 'r')
    outputFile = open(outputFileName, 'w')
    iter_f = iter(inputFile)
    for line in iter_f:
        record = line.split()
        length = len(record)
        if length == 10:
            outputFile.write(line)

    inputFile.close()
    outputFile.close()