#-*- coding: utf-8 -*-
# compute the diversity of each pair
from __future__ import division
import os
import math

data_src = "/Users/ghostchef/data/shcool-card-data/"
# freq_file = open(data_src + 'strength/cooc-freq.txt', 'r')
freq_file = open(data_src + 'strength/weight_freq.txt', 'r')
cooc_freq = dict()
entropy = dict()

#compute weighted frequency value
for line in freq_file.readlines():
    rec = line.split(':')
    info = eval(rec[0])
    tup = (info[0], info[1])
    # cooc_freq[tup] = int(rec[1])
    cooc_freq[tup] = float(rec[1])
freq_file.close()

local_weight = dict()
weight_file = open(data_src + 'cooc/norm_weight.txt', 'r')
for line in weight_file.readlines():
    rec = line.split(':')
    local_weight[rec[0]] = float(rec[1])
weight_file.close()


# outfile = open(data_src + 'strength/cooc_diversity.txt', 'w')
outfile = open(data_src + 'strength/weight_diversity.txt', 'w')
freq_file = open(data_src + 'cooc/local-freq-3.txt', 'r')

for line in freq_file.readlines():
    rec = line.split(':')
    info = eval(rec[0])
    tup = (info[0], info[1])
    # p_ij = int(rec[1]) / cooc_freq[tup]
    p_ij = ( float(rec[1]) * local_weight[rec[0]]) / cooc_freq[tup]

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