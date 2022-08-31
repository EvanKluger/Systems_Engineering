# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 15:07:21 2022

@author: jklug

Model of Cessna Plane for SYstems Engineering Final
"""

from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as LA
import math

plt.close('all')

# states: u (body vel), alpha (AOA), theta (pitch angle), q (pitch vel)
A = np.array([
   [-0.0317,    0.0671,   -0.1638,         0],
   [-0.3254,   -0.7391,         0,   28.6803],
   [      0,         0,         0,   29.6241],
   [0.0060,   -0.0497,         0,  -1.5633]
    ])
# inputs: delta_e (elevator), delta_T (thrust)
B = np.array([
         [0],
   [-0.0893],
   [      0],
   [-0.2269]
])
C = np.eye(4)
D = np.zeros((4,1))

sys = ss(A, B, C, D)
t = np.linspace(0, 100, 1000)
t2 = np.array([[0,0],
               [0,0]
               ])


y, t = impulse(sys, t)
u1 = y[:,0]
a1 = y[:,1]
theta1 = y[:,2]
q1 = y[:,3]
plt.figure()
plt.plot(t, u1, label=r'$u: Longitudinal Velocity $')
plt.plot(t, a1, label=r'$a: angle of attack (angle of aircraft to air velocity vector)$')
plt.plot(t, theta1, label=r'$\theta: pitch angle (angle of aircraft to horizontral plane$')
plt.plot(t, q1, label=r'$q: angular pitch velocity$')
plt.xlabel('$t [s]$')
plt.ylabel('y [units differ for individual data]')
plt.legend()
plt.title('Cessna Motion Analysis: Impulse Response')
plt.show()




#y3 = 200*math.e**((y2[1])*t)
#plt.figure()
#plt.plot(t, y3, label='$steady state first order solution$')



p = pole(sys)

plt.figure()
plt.plot(np.real(p), np.imag(p),'x')
plt.xlabel('Real')
plt.ylabel('Imag')
plt.title('Pole plot')


x0 = np.array([
    [.0036],
    [0],
    [.2661],
    [-.031],
])

y4, t = initial(sys, t, x0)
u2 = y4[:,0]
a2 = y4[:,1]
theta2 = y4[:,2]
q2 = y4[:,3]
plt.figure()
plt.plot(t, u2, label=r'$u: Longitudinal Velocity $')
plt.plot(t, a2, label=r'$\alpha: angle of attack (angle of aircraft to air velocity vector)$')
plt.plot(t, theta2, label=r'$\theta: pitch angle (angle of aircraft to horizontral plane$')
plt.plot(t, q2, label=r'$q: angular pitch velocity$')
plt.xlabel('$t [s]$')
plt.ylabel('y ')
plt.legend()
plt.title('Cessna Motion Analysis:Initial Response')
plt.show()
