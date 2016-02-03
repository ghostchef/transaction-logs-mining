#-*- coding: utf-8 -*-
# compute the weight of a co-occurrence
from __future__ import division
import os
import math

data_src = "/Users/ghostchef/data/shcool-card-data/"
files = os.listdir(data_src + 'group/')

# compute weight of a location
loc_weight = dict() # dict for weight of each location{str : float}

for fi in files:
    if fi[0] != '.':
        file = open(data_src + 'group/' + fi)
        v_ul = dict()
        p_lu = dict()
        loc = fi.split('.')[0][6:]
        h_l = 0.0
        w_l = 0.0

        logs = file.readlines()
        v_l = len(logs)

        # for location with less than 40 records, give a w_l value 0.05 directly
        if v_l > 40:
            for log in logs:
                record = log.split()
                if v_ul.has_key(record[0]):
                    v_ul[record[0]] += 1
                else:
                    v_ul[record[0]] = 1

            # compute p_lu
            for user, times in v_ul.iteritems():
                p_lu[user] = times / v_l

            # compute entropy
            for k, v in p_lu.iteritems():
                h_l += (v * math.log(v))

            # compute weight of location
            w_l = math.exp(h_l)
        else:
            w_l = 0.05

        loc_weight[loc] = w_l

loc_weight_file = open(data_src+'loc_weight.txt', 'w')

for k, v in loc_weight.iteritems():
    loc_weight_file.write(k+','+str(v)+'\n')

