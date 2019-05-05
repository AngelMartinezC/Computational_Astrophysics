#-*- coding: utf-8 -*-

"""
  Lagrange interpolation
"""

import numpy as np
import matplotlib.pyplot as plt


# Define interpolation
def lagrange(function,x,n):
	punto = len(x) - 1
	def prod(n,j):
		con = 1
		for k in range(0,n+1):
			if k != j:
				con = con*(x-x[int(k*punto/n)])/(x[int(j*punto/n)]-x[int(k*punto/n)])			
			else:
				pass
		return np.array(con)
	a = 0
	for j in range(0,n+1):
		a += np.array(function(x[int(j*punto/n)])*prod(n,j))
	return a

class derivative:
	# Define derivatives
	def backward(f,x0=0.2,step=0.2):
		return(f(x0) - f(x0-step))/step

	def forward(f,x0=0.2,step=0.2):
		return (f(x0+step) - f(x0))/step

	def central(f,x0=0.2,step=0.2):
		return (f(x0+step) - f(x0-step))/(2*step)


if __name__ == '__main__':


	# Define function
	def f(x):
		return np.array(1/(25*x**2 +1))
	
	# Define domain
	x = np.linspace(-1.0,1.0,1000)	
	points = [6,8,10,12]

	plt.ylim((-2,2))
	plt.plot(x,f(x),linewidth=3,color='b',label=r'$f(x)$')
	for i in points:
		y = lagrange(f,x,n=i)
		plt.plot(x,y,label='n='+str(i))
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.savefig('4a.png')
	plt.show()

