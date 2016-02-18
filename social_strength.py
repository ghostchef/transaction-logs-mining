#-*- coding: utf-8 -*-
# compute the social strength of given pair
from __future__ import division
import os
import math

data_src = "/Users/ghostchef/data/shcool-card-data/strength/"

freq = dict()
divr = dict()
max_freq = 0.0
max_divr = 0.0

# freq_file = open(data_src + 'cooc_freq.txt', 'r')
# divr_file = open(data_src + 'cooc_diversity.txt', 'r')
# coef_file = open(data_src + 'cooc_coef.txt', 'r')
# strength_file = open(data_src + 'cooc_strength.txt', 'w')

freq_file = open(data_src + 'weight_freq.txt', 'r')
divr_file = open(data_src + 'weight_diversity.txt', 'r')
coef_file = open(data_src + 'weight_coef.txt', 'r')
strength_file = open(data_src + 'weight_strength.txt', 'w')

for line in freq_file.readlines():
    rec = line.split(':')
    freq[rec[0]] = float(rec[1])
    if max_freq < float(rec[1]):
        max_freq = float(rec[1])
freq_file.close()

for line in divr_file.readlines():
    rec = line.split(':')
    divr[rec[0]] = float(rec[1])
    if max_divr < float(rec[1]):
        max_divr = float(rec[1])
divr_file.close()

for line in coef_file.readlines():
    rec = line.split(':')
    # strength = ( float(rec[1]) + ((freq[rec[0]] - 3)/(max_freq - 3)) + ((divr[rec[0]] - 1)/(max_divr - 1)) ) / 3
    strength = ( float(rec[1]) + ((freq[rec[0]])/(max_freq )) + ((divr[rec[0]] - 1)/(max_divr - 1)) ) / 3
    strength_file.write(rec[0] + ':' + str(strength) + '\n')
coef_file.close()
strength_file.close()
print max_divr
print max_freq