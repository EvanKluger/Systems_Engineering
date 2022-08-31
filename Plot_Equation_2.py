# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 22:19:57 2022

@author: jklug
"""

import numpy as np
import matplotlib.pyplot as plt
from control.matlab import * 
import control.matlab as mt # MATLAB-like control toolbox functionality
t = np.linspace(0,10,100)
y = (2.718**(-t/2))*(4*np.sin(t/2))


fig, ax = plt.subplots()
ax.plot(t,y)
ax.set(title='4C: Plot of Solution ')
ax.set_ylabel('y')
ax.set_xlabel('Time [s]')
