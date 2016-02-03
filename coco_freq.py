#-*- coding: utf-8 -*-
# compute frequency of two user for all location

data_src = "/Users/ghostchef/data/shcool-card-data/"

freq_dict = dict()
file = open(data_src+'local-freq-all.txt', 'r')

# count cooc frequency
for line in file.readlines():
    rec = line.split(':')
    info = eval(rec[0])
    freq = int(rec[1])
    tup = (info[0], info[1])

    if freq_dict.has_key(tup):
        freq_dict[tup] += freq
    else:
        freq_dict[tup] = freq

file.close()

# write co-occurrence frequency into file
freq_file = open(data_src+'cooc-freq-all.txt', 'w')
for k, v in freq_dict.iteritems():
    freq_file.write( str(k) + ":" + str(v) +'\n')