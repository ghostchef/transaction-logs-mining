#-*- coding: utf-8 -*-
# some test code for python feature
import os

data_src = "/Users/ghostchef/data/shcool-card-data/"

file = open(data_src+'cooc-freq-all.txt', 'r')
outfile = open(data_src+'thod-freq-3.txt', 'w')

# count cooc frequency
for line in file.readlines():
    rec = line.split(':')
    freq = int(rec[1])

    if freq > 2:
        outfile.write(line)

file.close()