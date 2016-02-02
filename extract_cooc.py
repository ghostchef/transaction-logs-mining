#-*- coding: utf-8 -*-
# extracting co-occurrence from transaction log sequences.
import os
import sys

def median(lst):
    if not lst:
        return
    lst = sorted(lst)
    if len(lst) % 2 == 1:
        return lst[ len(lst) // 2 ]
    else:
        return lst[ (len(lst) // 2) - 1]

data_src = "/Users/ghostchef/data/shcool-card-data/"
files = os.listdir(data_src + 'group/')

# dict for store local frequency of co-occurrence
cooc_dict = dict()

# traversal all transaction logs sequence file
for fi in files:
    # ignore hidden files
    if fi[0] != '.':
        # process one log sequence
        file = open(data_src+'group/'+fi)
        log_list = file.readlines()
        time_gap_list = []

        print "processing file: " + fi

        # ignore group with only on transaction log
        if len(log_list) > 1:
            # compute the time co-occurrence threshold
            for index in range(1, len(log_list)):
                time_1 = int(log_list[index].split()[3])
                time_2 = int(log_list[index-1].split()[3])
                time_gap_list.append(abs(time_1 - time_2))
            mid = median(time_gap_list)

            # extracting co-occurrence
            for index in range(0, len(log_list) - 1):
                temp_index = index + 1
                while temp_index < len(log_list) and int(log_list[temp_index].split()[3]) - int(log_list[index].split()[3]) <= mid:
                    if log_list[temp_index].split()[0] != log_list[index].split()[0]:
                        co_oc = (log_list[temp_index].split()[0], log_list[index].split()[0], log_list[temp_index].split()[4])
                        co_co = (log_list[index].split()[0], log_list[temp_index].split()[0], log_list[temp_index].split()[4])
                        if cooc_dict.has_key(co_oc):
                            cooc_dict[co_oc] += 1
                            cooc_dict[co_co] += 1
                        else:
                            cooc_dict[co_oc] = 1
                            cooc_dict[co_co] = 1
                    temp_index += 1

        file.close()

local_freq = open(data_src+'local-freq-all.txt', 'w')
for k, v in cooc_dict.iteritems():
    local_freq.write( str(k) + ":" + str(v) +'\n')
