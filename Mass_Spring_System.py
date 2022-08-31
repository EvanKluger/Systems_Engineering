import numpy as np
import matplotlib.pyplot as plt
from control.matlab import * 
import control.matlab as mt # MATLAB-like control toolbox functionality

plt.close('all')


wn = 1
z = .1
m = 1


A = np.array([
    [0, 1],
    [-wn**2,-2*z*wn]
    ])

B = np.array([
    [0],
    [1/m]
    ])

C = np.array([
    [1, 0]
    ])

D = 0  




sys = mt.ss(A,B,C,D)
#s = mt.tf('s')
#sys = (1/m)/(s**2 + 2*z*wn*s+wn**2 )
G = mt.tf(sys)
print(G)

sys_new = mt.ss(G)
print(sys_new)
# 10 unit Step Response
x0 = np.array([
    [1],
    [1]
    ])
T = np.linspace(0, 40, 400)


y, t = mt.step(sys, T, x0)
y = 10*y


fig, ax = plt.subplots()
ax.plot(t,y)
ax.set_ylabel('y [m]')
ax.set_xlabel('t [s]')



