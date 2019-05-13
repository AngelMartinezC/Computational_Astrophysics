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

def y(E,e,a=1.496e8):
	b=a*np.sqrt(1-e**2)
	return b*np.sin(E)


time = [91,182,273]
eccentricity = 0.0167
a=1.496e8
a1 = 0
b1 = 2*np.pi+1
T = 365.25635

#print('roots',bis.iteration(f,a1,b1,epsilon=1e-10))


print('\nPunto a')
for t in time:
	SOL=bis.bisection(f,a=a1,b=b1,e=eccentricity,w=2*np.pi/T,t=t,epsilon=1e-22)
	angle = SOL[0][0]
	print('For t: {}\n  E is {}\n  x is {} = {} AU\n  y is {} = {} AU\n  iterations  {}\n'.format(t,angle,x(E=angle),x(E=angle)/a,y(angle,e=eccentricity),y(angle,e=eccentricity)/a,SOL[1]))


print('\nPunto b')
for t in time:
	SOL=bis.bisection(f,a=a1,b=b1,e=1,w=2*np.pi/T,t=t,epsilon=1e-22)
	angle = SOL[0][0]
	print('For t: {}\n  E is {}\n  x is {} = {} AU\n  y is {} = {} AU\n  iterations  {}\n'.format(t,angle,x(E=angle),x(E=angle)/a,y(angle,e=eccentricity),y(angle,e=eccentricity)/a,SOL[1]))


