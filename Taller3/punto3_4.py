#-*- coding: utf-8 -*-

"""
  Second derivate at a point and for a function
"""

import numpy as np
import matplotlib.pyplot as plt


# Define function
def f(x):
	return x-np.sin(x)


# Define derivative

# First derivative
def central(x0=0.2,step=0.2):
	return (f(x0+step) - f(x0-step))/(2*step)

# Second derivative
def central2(x0=0.2,step=0.2):
	return (f(x0+step) + f(x0-step)-2*f(x0))/(step**2)

# Analytical derivative
def deri2(x):
	return np.sin(x)


# Derivative in a range
def derivative(der,step=0.1):	
	f = open('derivative2.txt','w')
	y,x = [],[]
	for i in np.arange(-1,1,step):
		y.append(der(x0=i,step=step))
		x.append(i)
		f.write(str(i) + ' ' + str(der(x0=i,step=step))+'\n')
	f.close()
	return x,y

print(' Second derivative at x=0: ',central2(x0=0,step=0.2))

X = np.linspace(-1,1,100)
x1, y1 = derivative(central)
x2, y2 = derivative(central2)
s,t = np.loadtxt('derivative2.txt',unpack=True)

# Plots
plt.title('Punto 4a')
plt.plot(X,f(X),linewidth=2,label='f(x) = x - sin x')
plt.ylabel('y')
plt.xlabel('x')
plt.plot(x1,y1,'o-',label='f$^{(1)}$(x)')
plt.plot(s,t,'o-',label='f$^{(2)}$(x)')
plt.legend()
plt.savefig('4a.png')
plt.show()

plt.title('Punto 4b')
plt.plot(X,f(X),linewidth=2,label='f(x) = x - sin x')
plt.ylabel('y')
plt.xlabel('x')
plt.plot(s,t,'o-',label='f$^{(2)}$(x) ')
plt.plot(X, deri2(X),label='f(x) = sin x')
plt.legend()
plt.savefig('4b.png')
plt.show()




