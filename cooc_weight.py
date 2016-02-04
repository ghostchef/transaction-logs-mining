#-*- coding: utf-8 -*-
# compute the weight of a co-occurrence
from __future__ import division
import os
import math

data_src = "/Users/ghostchef/data/shcool-card-data/"


# compute weight of a location
loc_weight = dict() # dict for weight of each location: {str : float}
nom_loc_weight = dict() # normalized weight of frequency
files = os.listdir(data_src + 'group/')

v_u = dict() # count the total visit number of a user: {user : times}
v_ul = dict() # count visit numbers of a user to a location

for fi in files:
    if fi[0] != '.':
        print "we are processing: " + fi
        file = open(data_src + 'group/' + fi)
        p_lu = dict()
        loc = fi.split('.')[0][6:]
        h_l = 0.0
        w_l = 0.0

        logs = file.readlines()
        v_l = len(logs)

        for log in logs:
            record = log.split()
            # count v_ul
            if v_ul.has_key((record[0], loc)):
                v_ul[(record[0], loc)] += 1
            else:
                v_ul[(record[0], loc)] = 1

            # count v_u
            if v_u.has_key(record[0]):
                v_u[record[0]] += 1
            else:
                v_u[record[0]] = 1

#         # compute p_lu: the probability of a location visited by a user among other users
#         for user, times in v_ul.iteritems():
#             if user[1] == loc:
#                 p_lu[user] = times / v_l
#
#         # compute entropy
#         for k, v in p_lu.iteritems():
#             h_l += (v * math.log(v))
#
#         # compute weight of location
#         w_l = math.exp(h_l)
#         loc_weight[loc] = w_l
#
# for k, v in loc_weight.iteritems():
#     nom_loc_weight[k] = 100 * v
#
# loc_weight_file = open(data_src+'loc_weight.txt', 'w')
# for k, v in loc_weight.iteritems():
#     loc_weight_file.write(k+','+str(v)+'\n')
#
# nor_loc_weight_file = open(data_src+'nom_loc_weight.txt', 'w')
# for k, v in nom_loc_weight.iteritems():
#     nor_loc_weight_file.write(k+','+str(v)+'\n')


# # compute p_ul: the probability of a user visit a location among other location
# p_ul = dict()
# for user, times_u in v_u.iteritems():
#     print "we are computing p_ul for user: " + user
#     for ul, times_ul in v_ul.iteritems():
#         if ul[0] == user:
#             p_ul[ul] = times_ul / times_u
#
# # compute w_uvl: weigh of a co-occurrence of two user at a location, personal weight
# w_uvl = dict()
# for k_1, v_1 in p_ul.iteritems():
#     for k_2, v_2 in p_ul.iteritems():
#         if k_1[1] == k_2[1]:
#             w_uvl[(k_1[0], k_2[0], k_1[1])] = -1 * math.log(v_1 * v_2)
#
# # write personal weight into file
# per_weight_file = open(data_src+'per_weight.txt', 'w')
# for k, v in w_uvl.iteritems():
#     per_weight_file.write(str(k) + ':' + str(v) + '\n')
