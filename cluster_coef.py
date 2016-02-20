#-*- coding: utf-8 -*-
# compute the cluster coefficient
from __future__ import division


data_src = "/Users/ghostchef/data/shcool-card-data/"
file = open(data_src + 'sorted_strength/weight-strength.txt', 'r')

K = 200000
clu_sum = 0.0

edge_set = set()
neighbor = dict()

for index in range(0, K):
    line = file.readline()
    rec = line.split(':')
    tup = eval(rec[0])
    edge_set.add(tup)
    if neighbor.has_key(tup[0]):
        neighbor[tup[0]].append(tup[1])
    else:
        neighbor[tup[0]] = [tup[1]]
file.close()

for k, v in neighbor.iteritems():
    if len(v) > 1:
        ek = 0
        for i in range(0, len(v)):
            for j in range(i, len(v)):
                tup = (v[i], v[j])
                if tup in edge_set:
                    ek += 1
        # print ek
        ck = (2 * ek) / (len(v) * (len(v) - 1))
        clu_sum += ck

print 'cluster sum: ' + str(clu_sum)
print 'cluster coefficient: ' + str(clu_sum / len(neighbor))

