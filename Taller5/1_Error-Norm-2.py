#-*- coding: utf-8 -*-

"""
  Computation of Error-Norm-2
"""

import numpy as np
import matplotlib.pyplot as plt
from interpolation import lagrange 


def f(x):
	return np.array(1/(25*x**2 +1))


def EN2(f,m,x,n=12):
	
	p = lagrange(f,x,n=n)
	rango = len(x)-1
	count = 0
	for i in range(0,m+1):
		fi = f(x[int(i*rango/m)])
		pi = p[int(i*rango/m)]
		count += ((pi-fi)/fi)**2
	
	EN = (1/m)*np.sqrt(count)
	return EN


if __name__=='__main__':

	# Define range and print error
	x = np.linspace(-1.0,1.0,1000)
	
	for i in [6,8,10,12]:
		err = EN2(f,m=100,x=x,n=i)
		print(" EN2  n={}:  {}".format(i,err))

