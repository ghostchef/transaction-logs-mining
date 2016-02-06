#-*- coding: utf-8 -*-
# compute the weight of a co-occurrence
from __future__ import division
import os
import math

data_src = "/Users/ghostchef/data/shcool-card-data/"

loc_weight = dict()
loc_weight_file = open(data_src + 'cooc/nom_loc_weight.txt', 'r')
prsn_weight_file = open(data_src + 'cooc/norm_wuvl.txt', 'r')
weight_file = open(data_src + 'cooc/norm_weight.txt', 'w')

for line in loc_weight_file.readlines():
    rec = line.split(',')
    loc_weight[rec[0]] = float(rec[1])
loc_weight_file.close()

for line in prsn_weight_file.readlines():
    rec = line.split(':')
    info = eval(rec[0])
    wgt = (float(rec[1]) + loc_weight[info[2]]) / 2
    weight_file.write(str(rec[0]) + ':' + str(wgt) + '\n')