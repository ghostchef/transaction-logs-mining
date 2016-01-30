#-*- coding: utf-8 -*-
import os

for index in range(1, 10):
    inputFileName = "/Users/ghostchef/workplace/python/GraduationThesis/logs/ykt_his_trade_20140" +str(index)+".txt"
    outputFileName = "/Users/ghostchef/workplace/python/GraduationThesis/logs/cleaned_20140"+ str(index) + ".txt"
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