#-*- coding: utf-8 -*-
# count log times of each user

import os

data_src = "/Users/ghostchef/data/shcool-card-data/"
files = os.listdir(data_src + 'cleaned-logs/')
log_count = dict()

for fi in files:
    if fi[0] != '.':
        print "we are processing: " + fi
        file = open(data_src + 'cleaned-logs/' + fi)
        for line in file.readlines():
            info = line.split()
            if log_count.has_key(info[1]):
                log_count[info[1]] += 1
            else:
                log_count[info[1]] = 1
        file.close()

log_count_file = open(data_src+'stuff/user_log_count.txt', 'w')
for k, v in log_count.iteritems():
    log_count_file.write(k + ' ' + str(v) + '\n')
log_count_file.close()