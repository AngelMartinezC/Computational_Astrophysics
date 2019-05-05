#-*- coding: utf-8 -*-

"""
 Program to calculate integral
"""

import numpy as np
import matplotlib.pyplot as plt


# Function to calculate the integral
def f(x):
	return x*np.sin(x)

# Integral
def integral(f,a=0,b=np.pi,N=100,method='midpoint'):
	x = np.linspace(a,b,10000)
	rango = len(x)-1
	integral = 0
	for i in range(0,N):
		ai = x[int(i*rango/N)]
		bi = x[int((i+1)*rango/N)]
		if method=='midpoint':
			y = (bi-ai)*f((ai+bi)/2)
			integral += y
		elif method=='trapezoid':
			y = 0.5*(bi-ai)*(f(bi)+f(ai))
			integral += y
		elif method=='simpson':
			y = ((bi-ai)/6)*(f(ai)+4*f((ai+bi)/2)+f(bi))
			integral += y
		else:
			return None
	return integral	


if __name__=='__main__':

	# Results
	EM, ET, ES = [], [], []
	result = np.pi
	for i in [1,2,5,10,20,50,100,1000]:
		M = integral(f,N=i,method='midpoint')
		T = integral(f,N=i,method='trapezoid')
		S = integral(f,N=i,method='simpson')
		eM = 100*abs(M-result)/result
		eT = 100*abs(T-result)/result
		eS = 100*abs(S-result)/result
		EM.append(eM)
		ET.append(eT)
		ES.append(eS)
		print(' N:           {}'.format(i))
		print(' Step:        {}'.format(np.pi/i))
		print(' Midpoint:    {}  {}'.format(M,eM))
		print(' Trapezoidal: {}  {}'.format(T,eT))
		print(' Simpson:     {}  {}\n'.format(S,eS))
		







































