# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 01:29:49 2019

@author: Mudassir Kidwai
"""

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.title('Voltage - Time')
plt.xlabel('time (sec)')
plt.ylabel('voltage (mV)')

#Showing the grids
plt.grid(True)

#Saving the file
plt.savefig("test.png")

#Showing the plot
plt.show()