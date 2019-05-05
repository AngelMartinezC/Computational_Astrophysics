#-*- coding: utf-8 -*-

"""
  Computation of linear stepwise interpolation
"""

import numpy as np
import matplotlib.pyplot as plt
from interpolation import derivative as d


def f(x):
	return np.array(1/(25*x**2 +1))


def linear(x,m=50):
	
	point = len(x) -1
		
	Y, X = [], []	
	x_tot = []
	y_tot = []
	for k in range(0,m):
		# Define sub-range of x array
		s = x[int(k*point/m)] 
		function = f(x[int(k*point/m)])
		# Line equation rápido
		x_t = np.linspace(x[int(k*point/m)],x[int((k+1)*point/m)],10)
		M = (f(x[int((k+1)*point/m)])-f(x[int(k*point/m)]))/(x[int((k+1)*point/m)]-s)
		b = f(x[int(k*point/m)]) - M*x[int(k*point/m)]
		
		x_tot.extend(x_t)
		y_tot.extend(M*x_t+b)
		X.append(s)
		Y.append(function)
		
	return X, Y, x_tot,y_tot
	
m = 50
x_range = np.linspace(-1,1,1000)
x, y, x_t, y_t = linear(x_range,m=m)


plt.figure(figsize=(9,6))
markers_on = list(np.arange(0,m,1))
plt.plot(x_range,f(x_range),linewidth=3.0,label=r'Función f(x) = $(25x^2+1)^{-1}$')
plt.plot(x,y,'--',marker='D',markevery=markers_on,linewidth=2.0,label='Piecewise Linear Interpolation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.savefig('Linear_Interpolation.png')
plt.show()


### Putno b  rápido -------


def EN2(f,m,x,n=12):
	
	rango = len(x)-1
	rangoy = len(y_t)-1
	count = 0
	for i in range(0,m+1):
		fi = f(x[int(i*rango/m)])
		pi = y_t[int(i*rangoy/m)]
		count += ((pi-fi)/fi)**2
	
	EN = (1/m)*np.sqrt(count)
	return EN

err = EN2(f,m=100,x=x_range)
print(" EN2  linear:  {}".format(err))


