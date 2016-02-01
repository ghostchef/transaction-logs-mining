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
log_count = 0
exclude_list = ['.', 'x']

consumerID_set = set([])
username_set = set([])
stuname_set = set([])
stu_count = 0
log_stu_count = 0

# process student profile: count student number and collect names
stu_file = data_src + "original-logs/xs_ykt.xls"
data = xlrd.open_workbook(stu_file)
table = data.sheets()[0]
stu_count = table.nrows - 1
for i in range(1, table.nrows):
    row = table.row_values(i)
    # encode to utf-8 before add to set
    stuname_set.add(unicode(row[6]).encode('utf-8'))


# process log files: count consumer numbers and collect names and ID
for file in files:
    cur_file = open(path+file, 'r')
    for line in cur_file.readlines():
        record = line.split()
        consumerID_set.add(record[1])
        username_set.add(record[2])
    cur_file.close()
log_stu_count = len(consumerID_set)

name_combine_set = username_set & stuname_set

print "profile student count: " + str(stu_count)
print "logs student count: " + str(log_stu_count)
print "profile student name count: " + str(len(stuname_set))
print "logs student name count: " + str(len(username_set))
print "combine name count: " + str(len(name_combine_set))

profile_names = open(data_src+"profile_names.txt", 'w')
log_names = open(data_src+ "log_names.txt", 'w')
combine_names = open(data_src+ "combine_names.txt", 'w')


for name in stuname_set:
    profile_names.write(str(name)+'\n')

for name in username_set:
    log_names.write(str(name)+'\n')

for name in name_combine_set:
    combine_names.write(str(name)+'\n')
# # count log numbers
# for f in files:
#     if f[0] not in exclude_list:
#         curr_file = open(path + f, 'r')
#         count = len(curr_file.readlines())
#         log_count += count - 1
#         curr_file.close()
#
# print log_count