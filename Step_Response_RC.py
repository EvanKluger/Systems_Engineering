# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 22:01:56 2022

@author: jklug
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 20:51:24 2022

@author: jklug
"""

import numpy as np
import matplotlib.pyplot as plt
from control.matlab import * 
import control.matlab as mt # MATLAB-like control toolbox functionality

plt.close('all')

Qin = 1
C = .000001
R = 100000
Vin = 1
A = np.array([
    [-2/(R*C)]
    ])

B = np.array([
    [Vin/(R*C)]
    ])

C = np.array([
    [1]
    ])

D = np.array([
    [0]
    ])



sys = mt.ss(A,B,C,D)


x0 = np.array([
    [0]
    ])

T = np.linspace(0, .6, 1000)


y, t = mt.step(sys, T, x0)




fig, ax = plt.subplots()
ax.plot(t,y)
ax.set(title='2D: Step Response of RC Circuit ')
ax.set_ylabel('Vout[Vl')
ax.set_xlabel('Time [s]')







