#-*- coding: utf-8 -*-
# compute the social strength of given pair
from __future__ import division
import os
import math
import random

data_src = "/Users/ghostchef/data/shcool-card-data/"

pair_num = 205170
ID_list = []
random_pair = set()

profile_file = open(data_src + 'profile/log_ID_name.txt', 'r')
random_pair_file = open(data_src + 'strength/random_pair.txt', 'w')

for line in profile_file.readlines():
    rec = line.split(':')
    ID_list.append(rec[0])
profile_file.close()

while len(random_pair) < pair_num:
    rand_1 = random.randint(0, len(ID_list)-1)
    rand_2 = random.randint(0, len(ID_list)-1)
    if rand_1 != rand_2:
        tup = (ID_list[rand_1], ID_list[rand_2])
        random_pair.add(tup)

for tup in random_pair:
    random_pair_file.write(str(tup) + '\n')
random_pair_file.close()