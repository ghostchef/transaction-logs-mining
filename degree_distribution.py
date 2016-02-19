#-*- coding: utf-8 -*-
# compute the degree distribution
from __future__ import division


data_src = "/Users/ghostchef/data/shcool-card-data/"
file = open(data_src + 'sorted_strength/weight-strength.txt', 'r')

K = 100000
deg_dict = dict()

for index in range(0, K):
    line = file.readline()
    rec = line.split(':')
    tup = eval(rec[0])
    if deg_dict.has_key(tup[0]):
        deg_dict[tup[0]] += 1
    else:
        deg_dict[tup[0]] = 1
file.close()

outfile = open(data_src + 'degree_distribution.txt', 'w')
for k, v in deg_dict.iteritems():
    outfile.write(k + ':' + str(v) + '\n')
outfile.close()