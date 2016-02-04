#-*- coding: utf-8 -*-
# compute the weight of a co-occurrence
from __future__ import division
import os
import math

data_src = "/Users/ghostchef/data/shcool-card-data/"


# compute weight of a location
loc_weight = dict() # dict for weight of each location: {str : float}
nom_loc_weight = dict() # normalized weight of frequency
v_u = dict() # count the total visit number of a user: {user : times}
p_ul = dict() #the probability of a user visit a location among other location
w_uvl = dict()
files = os.listdir(data_src + 'group/')

# compute v_u
for fi in files:
    if fi[0] != '.':
        file = open(data_src + 'group/' + fi)
        loc = fi.split('.')[0][6:]
        logs = file.readlines()

        for log in logs:
            record = log.split()

            if v_u.has_key(record[0]):
                v_u[record[0]] += 1
            else:
                v_u[record[0]] = 1
        file.close()
print "v_u finished "

# compute v_ul and related
for fi in files:
    if fi[0] != '.':
        print "we are processing: " + fi
        file = open(data_src + 'group/' + fi)
        p_lu = dict()
        v_ul = dict() # count visit numbers of a user to a location
        loc = fi.split('.')[0][6:]
        h_l = 0.0
        w_l = 0.0

        logs = file.readlines()
        v_l = len(logs)

        for log in logs:
            record = log.split()
            # count v_ul
            if v_ul.has_key(record[0]):
                v_ul[record[0]] += 1
            else:
                v_ul[record[0]] = 1
        file.close()

        # compute p_ul
        for user, times in v_ul.iteritems():
            p_ul[(user, loc)] = times / v_u[user]


        # compute p_lu: the probability of a location visited by a user among other users
        for user, times in v_ul.iteritems():
            p_lu[user] = times / v_l

        # compute entropy
        for k, v in p_lu.iteritems():
            h_l += (v * math.log(v))

        # compute weight of location
        w_l = math.exp(h_l)
        loc_weight[loc] = w_l

# normalize location weight and write into files
for k, v in loc_weight.iteritems():
    nom_loc_weight[k] = 100 * v

loc_weight_file = open(data_src+'loc_weight.txt', 'w')
for k, v in loc_weight.iteritems():
    loc_weight_file.write(k+','+str(v)+'\n')
loc_weight_file.close()

nor_loc_weight_file = open(data_src+'nom_loc_weight.txt', 'w')
for k, v in nom_loc_weight.iteritems():
    nor_loc_weight_file.write(k+','+str(v)+'\n')
nor_loc_weight_file.close()

# copy list
pul_list_1 = []
pul_list_2 = []
for k, v in p_ul.iteritems():
    pul_list_1.append((k, v))
    pul_list_2.append((k, v))

# computing w_uvl"
per_weight_file = open(data_src+'personal_weight.txt', 'w')
for i in range(0, len(pul_list_1)):
    for j in range(i+1, len(pul_list_2)):
        if pul_list_1[i][0][1] ==  pul_list_2[j][0][1] and pul_list_1[i][0][0] != pul_list_2[j][0][0]:
            w_uvl_v = -1 * math.log(pul_list_1[i][1] * pul_list_2[j][1])
            per_weight_file.write(str((pul_list_1[i][0][0], pul_list_2[j][0][0], pul_list_2[j][0][1]))+ ':' + str(w_uvl_v) + '\n')
per_weight_file.close()