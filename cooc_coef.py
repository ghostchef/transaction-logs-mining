#-*- coding: utf-8 -*-
# compute the coefficient of each pair
from __future__ import division
import os
import math

data_src = "/Users/ghostchef/data/shcool-card-data/"
# freq_file = open(data_src + 'cooc/cooc-freq-3.txt', 'r')
freq_file = open(data_src + 'strength/weight_freq.txt', 'r')
user_freq = dict()

#compute weighted frequency value
for line in freq_file.readlines():
    rec = line.split(':')
    info = eval(rec[0])
    if user_freq.has_key(info[0]):
        # user_freq[info[0]] += int(rec[1])
        user_freq[info[0]] += float(rec[1])
    else:
        # user_freq[info[0]] = int(rec[1])
        user_freq[info[0]] = float(rec[1])
freq_file.close()

# outfile = open(data_src + 'strength/cooc_coef.txt', 'w')
outfile = open(data_src + 'strength/weight_coef.txt', 'w')

# freq_file = open(data_src + 'cooc/cooc-freq-3.txt', 'r')
freq_file = open(data_src + 'strength/weight_freq.txt', 'r')

for line in freq_file.readlines():
    rec = line.split(':')
    info = eval(rec[0])
    tup = (info[0], info[1])
    # coef = int(rec[1]) / min(user_freq[info[0]], user_freq[info[1]])
    coef = float(rec[1]) / min(user_freq[info[0]], user_freq[info[1]])
    outfile.write(rec[0] + ':' + str(coef) + '\n')

freq_file.close()


