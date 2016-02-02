#-*- coding: utf-8 -*-
import os
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

data_src = "/Users/ghostchef/data/shcool-card-data/"

sp_list = ["开水房", "浴室"]

# line = "启秀开水房"
# line = "南山浴室"
line = "中华食堂"

type = 0

for word in sp_list:
    if word in line:
        type = 1

print type
