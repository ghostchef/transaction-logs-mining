#-*- coding: utf-8 -*-
# compute the co-class-rate of given network
from __future__ import division
import xlrd
import sys
import os

reload(sys)
sys.setdefaultencoding( "utf-8" )
data_src = "/Users/ghostchef/data/shcool-card-data/"

profile = dict()
class_info = dict()
profile_file = open(data_src + 'profile/log_ID_name.txt', 'r')

for line in profile_file.readlines():
    rec = line.split(':')
    profile[rec[0]] = rec[1][0:-1]
profile_file.close()

prof_file = data_src + "original-logs/xs_ykt.xls"
data = xlrd.open_workbook(prof_file)
table = data.sheets()[0]
for i in range(1, table.nrows):
    row = table.row_values(i)

    if class_info.has_key(unicode(row[3]).encode('utf-8')):
        class_info[unicode(row[3]).encode('utf-8')].add(unicode(row[6]).encode('utf-8'))
    else:
        class_info[unicode(row[3]).encode('utf-8')] = {unicode(row[6]).encode('utf-8')}


# compute co-class rate

break_point = [200, 2000, 10000, 20000, 40000, 60000, 80000, 100000, 200000, 300000, 400000, 410340]

#
# path = data_src + "sorted_strength/"
# files = os.listdir(path)
# for f in files:
#     if f[0] != '.':
#         file = open(data_src + 'sorted_strength/' + f, 'r')
#         outfile = open(data_src + 'co-class/' +f, 'w')
#         print 'we are processing file ' + f
#         hit_num = 0
#         for i in range(0, 410340):
#             line = file.readline()
#             rec = line.split(':')
#             tup = eval(rec[0])
#             name_1 = profile[tup[0]]
#             name_2 = profile[tup[1]]
#
#             for k, v in class_info.iteritems():
#                 if name_1 in v and name_2 in v:
#                     hit_num += 1
#                     break
#
#             for point in break_point:
#                 if i == point - 1:
#                     rate = hit_num / point
#                     outfile.write(str(point/2) + ':' + str(rate) + '\n')
#         file.close()
#         outfile.close()




# random guess co-class rate
print "we are computing co-class rate"
net_file = open(data_src + 'strength/random_pair.txt', 'r')
outfile = open(data_src + 'co-class/random_pair.txt', 'w')

hit_num = 0

for i in range(0, 205170):
    line = net_file.readline()
    tup = eval(line)
    name_1 = profile[tup[0]]
    name_2 = profile[tup[1]]

    for k, v in class_info.iteritems():
        if name_1 in v and name_2 in v:
            hit_num += 1
            break
    for point in break_point:
        if i == point - 1:
            rate = hit_num / point
            outfile.write(str(point/2) + ':' + str(rate) + '\n')
