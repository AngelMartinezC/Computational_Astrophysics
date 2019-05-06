#-*- coding: utf-8 -*-

"""
 Program to calculate the root plt
"""

import bisection as bis
import numpy as np
import matplotlib.pyplot as plt



def f(x,e=0.0167,w=2*np.pi/365.25635,t=91):
	y = x - e*np.sin(x)-w*t
	return y

def x(E,a=1.496e8):
	return a*np.cos(E)

def y(E,e):
	b=a*mp.sqrt(1-e**2)
	return b*np.sin(E)


time = [91,182,273]
eccentricity = 0.0167
a = 0
b = 2*np.pi

print('Punto a')
for t in time:
	SOLUTION=bis.bisection(f,a=a,b=b,e=eccentricity,w=2*np.pi/365.25635,t=t,epsilon=1e-22)
	print('For t: {}  the eccentric anomaly is {} iterations  {}'.format(t,SOLUTION[0],SOLUTION))


print('\nPunto b')
SOLUTION=bis.bisection(f,a=a,b=b,e=0.99999,w=2*np.pi/365.25635,t=190,epsilon=1e-22)
print(SOLUTION)


