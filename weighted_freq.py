#-*- coding: utf-8 -*-
# compute the weight of a co-occurrence
from __future__ import division
import os
import math

data_src = "/Users/ghostchef/data/shcool-card-data/"

freq_file = open(data_src + 'cooc/local-freq-3.txt', 'r')
wgt_file = open(data_src + 'cooc/norm_weight.txt', 'r')
wgt_freq_file = open(data_src + 'strength/weight_freq.txt', 'w')
weight = dict()
F_wgt_freq = dict()

# load weight file
for line in wgt_file.readlines():
    rec = line.split(':')
    weight[rec[0]] = float(rec[1])
wgt_file.close()


#compute weighted frequency value
print "computing weighted frequency"
for line in freq_file.readlines():
    rec = line.split(':')
    info = eval(rec[0])
    tup = (info[0], info[1])
    if F_wgt_freq.has_key(tup):
        F_wgt_freq[tup] += float(rec[1]) * weight[rec[0]]
    else:
        F_wgt_freq[tup] = float(rec[1]) * weight[rec[0]]
freq_file.close()

print "write into files"
for k, v in F_wgt_freq.iteritems():
    wgt_freq_file.write(str(k) + ':' + str(v) +  '\n')
wgt_freq_file.close()
