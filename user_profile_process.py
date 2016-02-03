#-*- coding: utf-8 -*-
import os
import xlrd
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )
data_src = "/Users/ghostchef/data/shcool-card-data/"
path = data_src + "cleaned-logs/"

files = os.listdir(path)
exclude_list = ['.', 'x']


# process student profile: count student number and collect names
prof_name_dict = dict()
class_dict = dict()
major_dict = dict()
shcool_dict = dict()
prof_file = data_src + "original-logs/xs_ykt.xls"
data = xlrd.open_workbook(prof_file)
table = data.sheets()[0]
for i in range(1, table.nrows):
    row = table.row_values(i)
    # encode to utf-8 before add to set
    # add record to name dict
    if prof_name_dict.has_key(unicode(row[5]).encode('utf-8')):
        pass
    else:
        prof_name_dict[unicode(row[5]).encode('utf-8')] = unicode(row[6]).encode('utf-8')

    # add record to class dict
    if class_dict.has_key(unicode(row[3]).encode('utf-8')):
        class_dict[unicode(row[3]).encode('utf-8')].add(unicode(row[6]).encode('utf-8'))
    else:
        class_dict[unicode(row[3]).encode('utf-8')] = {unicode(row[6]).encode('utf-8')}

    # add record to major dict
    if major_dict.has_key(unicode(row[7]).encode('utf-8')):
        major_dict[unicode(row[7]).encode('utf-8')].add(unicode(row[6]).encode('utf-8'))
    else:
        major_dict[unicode(row[7]).encode('utf-8')] = {unicode(row[6]).encode('utf-8')}

    # add record to school dict
    if shcool_dict.has_key(unicode(row[1]).encode('utf-8')):
        shcool_dict[unicode(row[1]).encode('utf-8')].add(unicode(row[6]).encode('utf-8'))
    else:
        shcool_dict[unicode(row[1]).encode('utf-8')] = {unicode(row[6]).encode('utf-8')}

# write profile info into files
prof_name_file = open(data_src+'prof_stuID_name.txt', 'w')
for k, v in prof_name_dict.iteritems():
    prof_name_file.write(k + ":" + v + '\n')
prof_name_file.close()

class_name_file = open(data_src+'class_member.txt', 'w')
for k, v in class_dict.iteritems():
    class_name_file.write(k + ":{")
    for name in v:
        class_name_file.write(name+', ')
    class_name_file.write("}\n")
class_name_file.close()

major_name_file = open(data_src+'major_member.txt', 'w')
for k, v in major_dict.iteritems():
    major_name_file.write(k + ":{")
    for name in v:
        major_name_file.write(name+', ')
    major_name_file.write("}\n")
major_name_file.close()

shcool_name_file = open(data_src+'school_member.txt', 'w')
for k, v in shcool_dict.iteritems():
    shcool_name_file.write(k + ":{")
    for name in v:
        shcool_name_file.write(name+', ')
    shcool_name_file.write("}\n")
shcool_name_file.close()



# process log files: count consumer numbers and build ID-name dict
log_name_dict = dict()
for file in files:
    cur_file = open(path+file, 'r')
    for line in cur_file.readlines():
        record = line.split()
        if log_name_dict.has_key(record[1]):
            pass
        else:
            log_name_dict[record[1]] = record[2]
    cur_file.close()

log_name_file = open(data_src+'log_ID_name.txt', 'w')
for k, v in log_name_dict.iteritems():
    log_name_file.write(k + ":" + v + '\n')



# count log numbers
log_count = 0
for f in files:
    if f[0] not in exclude_list:
        curr_file = open(path + f, 'r')
        count = len(curr_file.readlines())
        log_count += count
        curr_file.close()

print log_count
