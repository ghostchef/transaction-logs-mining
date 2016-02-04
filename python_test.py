#-*- coding: utf-8 -*-
# compute the weight of a co-occurrence
from __future__ import division
import os
import time
import math
data_src = "/Users/ghostchef/data/shcool-card-data/"


# compute personal weight: weight of a co-oc at location
files = os.listdir(data_src + 'group/')

v_u = dict() # count the total visit number of a user: {user : times}
v_ul = dict() # count visit numbers of a user to a location

for fi in files:
    if fi[0] != '.':
        print "we are processing: " + fi
        file = open(data_src + 'group/' + fi)
        loc = fi.split('.')[0][6:]
        logs = file.readlines()

        for log in logs:
            record = log.split()

            # count v_u
            if v_u.has_key(record[0]):
                v_u[record[0]] += 1
            else:
                v_u[record[0]] = 1
        file.close()
for k, v in v_u.iteritems():
    print str(k) + ":" + str(v) +"\n"




















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
