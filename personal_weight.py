#-*- coding: utf-8 -*-
# compute the weight of a co-occurrence
from __future__ import division
import os
import math

data_src = "/Users/ghostchef/data/shcool-card-data/"

## filter local cooc frequency
cooc_pair = set()
local_cooc = dict()
local_freq_file = open(data_src + 'cooc/local-freq-all.txt', 'r')
local_freq_cooc = open(data_src + 'cooc/local-freq-3.txt', 'w')
freq_file = open(data_src + 'cooc/cooc-freq-3.txt', 'r')

for line in freq_file.readlines():
    cooc = line.split(':')
    pair = eval(cooc[0])
    cooc_pair.add(pair)
freq_file.close()

for line in local_freq_file.readlines():
    cooc = line.split(':')
    cooc_loc = eval(cooc[0])
    pair = (cooc_loc[0], cooc_loc[1])
    if pair in cooc_pair:
        local_freq_cooc.write(line)
local_freq_cooc.close()
local_freq_file.close()


## compute personal weight
pul = open(data_src + 'cooc/pul.txt', 'r')
local_freq = open(data_src + 'cooc/local-freq-3.txt', 'r')
w_uvl = open(data_src + 'cooc/wuvl.txt', 'w')
pul_dict = dict()

print "loading pul"
for line in pul.readlines():
    rec = line.split(':')
    pul_dict[eval(rec[0])] = float(rec[1])
pul.close()

print "computing w_uvl"
max_wuvl = 0.0
min_wuvl = 100.0
for line in local_freq.readlines():
    cooc = line.split(':')
    info = eval(cooc[0])
    pul_1 = pul_dict[(info[0], info[2])]
    pul_2 = pul_dict[(info[1], info[2])]
    w_uvl_v = -1 * math.log(pul_1 * pul_2)
    if w_uvl_v > max_wuvl:
        max_wuvl = w_uvl_v
    if w_uvl_v < min_wuvl:
        min_wuvl = w_uvl_v
    w_uvl.write(str(info) + ":" + str(w_uvl_v)+"\n")
w_uvl.close()
local_freq.close()
print max_wuvl
print min_wuvl
