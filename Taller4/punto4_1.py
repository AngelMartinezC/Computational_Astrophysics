#-*- coding: utf-8 -*-

"""
  Lagrange interpolation
"""

import numpy as np
import matplotlib.pyplot as plt

# Define function
def f(x):
	return np.array(1/(25*x**2 +1))


# Define interpolation
def interpolation(function,x,n):

	puntos = len(x)
	punto = puntos -1
	
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

# Define domain
x = np.linspace(-1.0,1.0,1000)	
y1 = interpolation(f,x,n=6)
y2 = interpolation(f,x,n=8)
y3 = interpolation(f,x,n=10)
y4 = interpolation(f,x,n=12)

plt.ylim((-2,2))
plt.plot(x,f(x),linewidth=3,color='b',label=r'$f(x)$')
plt.plot(x,y1,label='n=6')
plt.plot(x,y2,label='n=8')
plt.plot(x,y3,label='n=10')
plt.plot(x,y4,label='n=12')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('4a.png')
plt.show()

