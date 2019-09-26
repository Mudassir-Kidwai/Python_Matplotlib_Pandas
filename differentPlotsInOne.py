# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 03:42:49 2019

@author: Mudassir Kidwai
"""

import matplotlib.pyplot as plt
import numpy as np

#np.random.seed(19680801)
np.random.seed(10)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(7,7))

axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()