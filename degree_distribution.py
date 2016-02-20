#-*- coding: utf-8 -*-
# compute the degree distribution
from __future__ import division


data_src = "/Users/ghostchef/data/shcool-card-data/"
file = open(data_src + 'sorted_strength/weight-strength.txt', 'r')

K = 410340
deg_dict = dict()
dist_dict = dict()

for index in range(0, K):
    line = file.readline()
    rec = line.split(':')
    tup = eval(rec[0])
    if deg_dict.has_key(tup[0]):
        deg_dict[tup[0]] += 1
    else:
        deg_dict[tup[0]] = 1
file.close()

print len(deg_dict)

# dist_file = open(data_src + 'dist_all.txt', 'w')
# outfile = open(data_src + 'deg_dst_all.txt', 'w')
# for k, v in deg_dict.iteritems():
#     if dist_dict.has_key(v):
#         dist_dict[v] += 1
#     else:
#         dist_dict[v] = 1
#     outfile.write(k + ':' + str(v) + '\n')
# outfile.close()
#
# for k, v in dist_dict.iteritems():
#     dist_file.write(str(k) + ':' + str(v) + '\n')
# dist_file.close()