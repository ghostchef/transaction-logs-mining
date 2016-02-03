#-*- coding: utf-8 -*-
# filter co-occurrence with frequency miner than threshold

data_src = "/Users/ghostchef/data/shcool-card-data/"
threshold = 4

file = open(data_src+'cooc-freq-all.txt', 'r')
outfile = open(data_src+'thod-freq-'+str(threshold)+'.txt', 'w')

# filter frequency
for line in file.readlines():
    rec = line.split(':')
    freq = int(rec[1])

    if freq > threshold:
        outfile.write(line)

file.close()