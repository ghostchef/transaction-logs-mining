#-*- coding: utf-8 -*-
# compute the weight of a co-occurrence
from __future__ import division
import os
import time
import math
import sys
import xlrd

reload(sys)
sys.setdefaultencoding( "utf-8" )

data_src = "/Users/ghostchef/data/shcool-card-data/"


file = open(data_src + 'sorted_strength/cooc-diversity.txt', 'r')
for i in range(0, 20):
    line = file.readline()
    print line
    rec = line.split(':')
    for j in range(0, len(rec)):
        print rec[j]


# prof_file = data_src + "stuff/strength.xlsx"
# data = xlrd.open_workbook(prof_file)
# for index in range(0, 8):
#     print "we are processing..."
#     outfile = open(data_src + 'sorted_strength/' + str(index) + '.txt', 'w')
#     table = data.sheets()[index]
#     for i in range(0, table.nrows):
#     # for i in range(0, 20):
#         row = table.row_values(i)
#         outfile.write(unicode(row[0]).encode('utf-8') + ':' + unicode(row[1]).encode('utf-8') + '\n')
#     outfile.close()


# # user log count
# count_dict = {100 : 0, 200 : 0, 300 : 0, 400 : 0, 500 : 0, 600 : 0, 700 : 0,
#               800 : 0, 900 : 0, 1000 : 0, 1100 : 0, 1200 : 0, 1300 : 0, 1400 : 0, 1500 : 0,
#               1600 : 0, 1700 : 0, 1800 : 0, 1900 : 0, 2000 : 0, 2100 : 0, 2200: 0,
#               2300: 0, 2400: 0, 2500: 0,}
#
# file = open(data_src+'stuff/user_log_count.txt', 'r')
# for line in file.readlines():
#     info = line.split()
#     count = int(info[1])
#     for k, v in count_dict.iteritems():
#         if k <= count:
#             count_dict[k] += 1
#
# outfile = open(data_src+'stuff/user_log_count_2.txt', 'w')
# for k, v in count_dict.iteritems():
#     outfile.write((str(k) + ' ' + str(v) + '\n'))
# outfile.close()


# # compute personal weight: weight of a co-oc at location
# files = os.listdir(data_src + 'group/')
#
# v_u = dict() # count the total visit number of a user: {user : times}
# v_ul = dict() # count visit numbers of a user to a location
#
# for fi in files:
#     if fi[0] != '.':
#         print "we are processing: " + fi
#         file = open(data_src + 'group/' + fi)
#         loc = fi.split('.')[0][6:]
#         logs = file.readlines()
#
#         for log in logs:
#             record = log.split()
#
#             # count v_u
#             if v_u.has_key(record[0]):
#                 v_u[record[0]] += 1
#             else:
#                 v_u[record[0]] = 1
#         file.close()
# for k, v in v_u.iteritems():
#     print str(k) + ":" + str(v) +"\n"


# # true division by: from __future__ import division
# a=2/3
# print a


# # string parse
# line = "('111724', '111747', '303'):2"
# lst = line.split(':')
# info = eval(lst[0])
# freq = int(lst[1])
#
# print lst
# print info
# print freq


# # timestamp transfer
# log_time = "2013-10-10 23:40:00"
# timeArray = time.strptime(log_time,'%Y-%m-%d %H:%M:%S')
# print timeArray
# log_time_stamp = int(time.mktime(timeArray))
# print log_time_stamp
#
# timeArray_2 = time.localtime(log_time_stamp)
# print timeArray_2
# otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_2)
# print otherStyleTime


# # Chinese check
# sp_list = ["开水房", "浴室"]
# # line = "启秀开水房"
# # line = "南山浴室"
# line = "中华食堂"
# type = 0
#
# for word in sp_list:
#     if word in line:
#         type = 1
# print type
