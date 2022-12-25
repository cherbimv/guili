import os
import csv
import glob

import string  # 引用glob
import numpy as np  # 引用numpy

line_max = 52
src_file = "classic/source/陈书"
tgt_file = "data/gu_chen.json"

g = open(tgt_file, "a", encoding="utf-8")

with open(src_file, "r", encoding="utf-8") as f:
    i = 1
    l1 = ""
    l2 = ""
    l3 = ""
    l4 = "说点什么"
    for line in f.readlines():
         line = line.strip("\n")
         if len(line) > line_max:
             continue;
         if i == 1:
             l1 = line
             l3 = ""
             d4 = dict(src_text=l4, tgt_text=l1)
             #print(d4)
             g.write(str(d4)+"\n")
             i = 2
         elif i == 2:
             l2 = line
             l4 = ""
             d1 = dict(src_text=l1, tgt_text=l2)
             g.write(str(d1) + "\n")
             #print(d1)
             i = 3
         elif i == 3:
             l3 = line
             d2 = dict(src_text=l2, tgt_text=l3)
             #print(d2)
             g.write(str(d2) + "\n")
             l1 = ""
             i = 4
         elif i == 4:
             l4 = line
             l2 = ""
             d3 = dict(src_text=l3, tgt_text=l4)
             g.write(str(d3) + "\n")
             #print(d3)
             i = 1
         else:
             break
f.close()