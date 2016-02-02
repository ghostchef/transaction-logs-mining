#-*- coding: utf-8 -*-
import os
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

data_src = "/Users/ghostchef/data/shcool-card-data/"
files = os.listdir(data_src + 'cleaned-logs/')
sp_list = ["开水", "浴室"]

group = dict()
group_index = 1

for file in files:
    if file[0] != '.':
        cur_file = open(data_src + 'cleaned-logs/' + file, 'r')
        print "we are processing " + file
        for line in cur_file.readlines():
            record = line.split()
            type = 0

            for word in sp_list:
                if word in record[4]:
                    type = 1

            if type == 1:
                group_ID = record[3]
            else:
                group_ID = record[3] + '_' + record[9]

            if group_ID in group:
                group[group_ID].append(line)
            else:
                group[group_ID] = []
                group[group_ID].append(line)

        cur_file.close()

for id, sequence in group.iteritems():
    outfile = open(data_src+"group/group_" + str(group_index) + ".txt", 'w')
    group_index += 1
    for log in sequence:
        outfile.write(log)
    outfile.close()