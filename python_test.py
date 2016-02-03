#-*- coding: utf-8 -*-
# some test code for python feature
import os
import time

data_src = "/Users/ghostchef/data/shcool-card-data/"


# string parse
line = "('111724', '111747', '303'):2"
lst = line.split(':')
info = eval(lst[0])
freq = int(lst[1])

print lst
print info
print freq




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
