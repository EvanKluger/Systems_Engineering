# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:54:53 2022

@author: jklug
"""

import numpy as np
import matplotlib.pyplot as plt
from control.matlab import * 
import control.matlab as mt # MATLAB-like control toolbox functionality
t = np.linspace(0,10,100)
y = (-2/3)*(2.718**(-3*t))+(2/3)
fig, ax = plt.subplots()
ax.plot(t,y)
ax.set(title='3B: Plot of Solution ')
ax.set_ylabel('y')
ax.set_xlabel('Time [s]')
