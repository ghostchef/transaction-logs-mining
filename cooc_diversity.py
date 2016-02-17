#-*- coding: utf-8 -*-
# compute the diversity of each pair
from __future__ import division
import os
import math

data_src = "/Users/ghostchef/data/shcool-card-data/"
freq_file = open(data_src + 'strength/cooc-freq.txt', 'r')
cooc_freq = dict()
entropy = dict()

#compute weighted frequency value
for line in freq_file.readlines():
    rec = line.split(':')
    info = eval(rec[0])
    tup = (info[0], info[1])
    cooc_freq[tup] = int(rec[1])
freq_file.close()


outfile = open(data_src + 'strength/cooc_diversity.txt', 'w')
freq_file = open(data_src + 'cooc/local-freq-3.txt', 'r')

for line in freq_file.readlines():
    rec = line.split(':')
    info = eval(rec[0])
    tup = (info[0], info[1])
    p_ij = int(rec[1]) / cooc_freq[tup]
    local_ent = p_ij * math.log(p_ij)
    if entropy.has_key(tup):
        entropy[tup] += local_ent
    else:
        entropy[tup] = local_ent
freq_file.close()

for k, v in entropy.iteritems():
    div = math.exp( -1 * v)
    outfile.write(str(k) + ':' + str(div) + '\n')
outfile.close()