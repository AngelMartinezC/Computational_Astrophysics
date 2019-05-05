#-*- coding: utf-8 -*-

"""
  Computation of Cubic Hermite
"""

import numpy as np
import matplotlib.pyplot as plt
#import interpolation as li
from interpolation import derivative as d


def f(x):
	return np.array(1/(25*x**2 +1))


def Hermite(x,m=50):
	
	point = len(x) -1
	def psi(z):
		psi0 = 2*z**3 - 3*z**2 + 1
		psi1 = z**3 - 2*z**2 + z
		return psi0,psi1
	
	derivative = []
	for k in range(0,m+1):
		if k == 0:
			derivative.append(d.forward(f,x[int(k*point/m)]))
		elif k == m:
			derivative.append(d.backward(f,x[int(k*point/m)]))
		else:
			derivative.append(d.central(f,x[int(k*point/m)]))
		
	cubic, X = [], []	
	for k in range(0,m):
		# Define sub-range of x array
		s = np.linspace(x[int(k*point/m)],x[int((k+1)*point/m)],10) 
		# z value
		z = (s-x[int(k*point/m)])/(x[int((k+1)*point/m)]-x[int(k*point/m)])
		# Hermite cubic fucntion
		H = f(x[int(k*point/m)])*psi(z)[0] + f(x[int((k+1)*point/m)])*psi(1-z)[0] +\
			derivative[k]*(x[int((k+1)*point/m)]-x[int(k*point/m)])*psi(z)[1] -\
			derivative[k+1]*(x[int((k+1)*point/m)]-x[int(k*point/m)])*psi(1-z)[1]
		
		X.extend(s)
		cubic.extend(H)
		
	return X, cubic
	
m = 21
x_range = np.linspace(-1,1,1000)
x,y = Hermite(x_range,m=m)


markers_on = list(np.linspace(0,10*(m-1),m,dtype=int))
plt.figure(figsize=(9,6))
plt.plot(x_range,f(x_range),linewidth=3.0,label=r'Función f(x) = $(25x^2+1)^{-1}$')
plt.plot(x,y,'--',marker='D',markevery=markers_on,linewidth=2.0,label='Cubic Hermite Interpolation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.savefig('Cubic_Hermite_Interpolation.png')
plt.show()





