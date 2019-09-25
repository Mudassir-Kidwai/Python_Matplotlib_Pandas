# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 02:08:20 2019

@author: Mudassir Kidwai
"""

import matplotlib.pyplot as plt

#plt.axes()

circle = plt.Circle((5, 0), radius=5, fc = 'Yellow')
plt.gca().add_patch(circle)
plt.grid(True)

plt.axis('scaled')
plt.show()