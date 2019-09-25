# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 02:34:39 2019

@author: Mudassir Kidwai
"""

import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 3
charlieBhai = (55, 40, 65)
JackieBhai = (62, 54, 20)
JerryBhai = (50,44,47)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
#opacity = 0.8

rects1 = plt.bar(index, charlieBhai, bar_width, color = 'b')
rects2 = plt.bar(index+bar_width, JackieBhai, bar_width, color = 'y')
rects3 = plt.bar(index+(2*bar_width), JerryBhai, bar_width, color = 'g')

plt.xlabel('Person') 
plt.ylabel('Scores')
plt.title('Scores by person')

#plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
plt.legend()
plt.tight_layout()
plt.show()