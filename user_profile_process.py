#-*- coding: utf-8 -*-
import os
import xlrd
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )
data_src = "/Users/ghostchef/data/shcool-card-data/"
path = data_src + "cleaned-logs/"
# path = data_src + "original-logs/"

files = os.listdir(path)
exclude_list = ['.', 'x']

log_name_dict = dict()
log_name_set = set([])
prof_name_set = set([])

prof_stu_count = 0
log_stu_count = 0
log_count = 0


# # process student profile: count student number and collect names
# stu_file = data_src + "original-logs/xs_ykt.xls"
# data = xlrd.open_workbook(stu_file)
# table = data.sheets()[0]
# stu_count = table.nrows - 1
# for i in range(1, table.nrows):
#     row = table.row_values(i)
#     # encode to utf-8 before add to set
#     prof_name_set.add(unicode(row[6]).encode('utf-8'))


# process log files: count consumer numbers and collect names and ID
for file in files:
    cur_file = open(path+file, 'r')
    for line in cur_file.readlines():
        record = line.split()
        if log_name_dict.has_key(record[1]):
            pass
        else:
            log_name_dict[record[1]] = record[2]
        # log_name_set.add(record[2])
    cur_file.close()

log_name_file = open(data_src+'log_ID_name.txt', 'w')
for k, v in log_name_dict.iteritems():
    log_name_file.write(k + ":" + v + '\n')

# log_stu_count = len(log_name_dict)
# name_combine_set = log_name_set & prof_name_set
#
# print "profile student count: " + str(prof_stu_count)
# print "logs student count: " + str(log_stu_count)
# print "profile student name count: " + str(len(prof_name_set))
# print "logs student name count: " + str(len(log_name_set))
# print "combine name count: " + str(len(name_combine_set))
#
# profile_names = open(data_src+"profile_names.txt", 'w')
# log_names = open(data_src+ "log_names.txt", 'w')
# combine_names = open(data_src+ "combine_names.txt", 'w')
#
# for name in prof_name_set:
#     profile_names.write(str(name)+'\n')
# for name in log_name_set:
#     log_names.write(str(name)+'\n')
# for name in name_combine_set:
#     combine_names.write(str(name)+'\n')


# # count log numbers
# for f in files:
#     if f[0] not in exclude_list:
#         curr_file = open(path + f, 'r')
#         count = len(curr_file.readlines())
#         log_count += count - 1
#         curr_file.close()
#
# print log_count













