# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 03:21:22 2019

@author: Mudassir Kidwai
"""

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted anti-clockwise:
labels = 'Cows', 'Bulls', 'Camels', 'Goats', 'Sheeps'
sizes = [10, 10, 30, 40, 10]
explode = (0,0,0,0,0)  # only "explode" the _ slice (i.e. ___)

fig1, apnaPie = plt.subplots()
apnaPie.pie(sizes,  explode=explode, labels = labels, autopct='%2.1f%%', shadow=True)
apnaPie.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
