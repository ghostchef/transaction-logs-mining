#-*- coding: utf-8 -*-
import os
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

data_src = "/Users/ghostchef/data/shcool-card-data/"
files = os.listdir(data_src + 'cleaned-logs/')

shop_dict = {}
pos_dict = {}
shopName_set = set([])
shopID_set = set([])
posID_set = set([])

for file in files:
    if file[0] != '.':
        cur_file = open(data_src + 'cleaned-logs/' + file, 'r')
        print "we are processing " + file
        for line in cur_file.readlines():
            record = line.split()
            shopID_set.add(record[3])
            posID_set.add(record[9])
            shopName_set.add(record[4])

            if record[3] not in shop_dict:
                shop_dict[record[3]] = record[4]
            if record[3] not in pos_dict:
                pos_dict[record[3]] = record[9]

        cur_file.close()

print "shopID counts: " + str(len(shopID_set))
print "shopName counts: " + str(len(shopName_set))
print "posID counts: " + str(len(posID_set))

shop_dict_file = open(data_src+'shop-dict.txt', 'w')
for d, x in shop_dict.items():
    shop_dict_file.write(unicode(str(d) + ":" + str(x) + '\n').encode('utf-8'))
shop_dict_file.close()

pos_dict_file = open(data_src+'pos-dict.txt', 'w')
for d, x in pos_dict.items():
    pos_dict_file.write(unicode(str(d) + ":" + str(x) + '\n').encode('utf-8'))
pos_dict_file.close()