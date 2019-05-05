#-*- coding: utf-8 -*-

"""
  First derivate at a point
"""

import numpy as np
import matplotlib.pyplot as plt


# Define function
def f(x):
	return x-np.sin(x)


# Define derivatives
def backward(x0=0.2,step=0.2):
	return(f(x0) - f(x0-step))/step

def forward(x0=0.2,step=0.2):
	return (f(x0+step) - f(x0))/step

def central(x0=0.2,step=0.2):
	return (f(x0+step) - f(x0-step))/(2*step)

# Analytical derivative
def deri(x):
	return 1-np.cos(x)


# Derivative in a range
def derivative(der,step=0.2):	
	f = open('derivative.txt','w')
	y,x = [],[]
	for i in np.arange(-1.0,1.1,step):
		y.append(der(x0=i,step=step))
		x.append(i)
		f.write(str(i) + ' ' + str(der(x0=i,step=step))+'\n')
	f.close()
	return x,y


X = np.linspace(-1.0,1.0,100)
x1, y1 = derivative(backward)
x2, y2 = derivative(forward)
x3, y3 = derivative(central)
#s,t = np.loadtxt('derivative.txt',unpack=True)


# Plots
plt.title('Punto 2a')
plt.plot(X,f(X),linewidth=2,label='f(x) = x - sin x')
plt.ylabel('y')
plt.xlabel('x')
plt.plot(x1,y1,'o-',label='backward')
plt.plot(x2,y2,'o-',label='forward')
plt.plot(x3,y3,'o-',label='central')
plt.legend()
plt.savefig('2a.png')
plt.show()

plt.title('Punto 2b')
plt.ylabel('1 - cosx')
plt.xlabel('x')
plt.plot(X,deri(X),linewidth=2,label='1 - cos x')
plt.plot(x1,y1,'o-',label='backward')
plt.plot(x2,y2,'o-',label='forward')
plt.plot(x3,y3,'o-',label='central')
plt.legend()
plt.savefig('2b.png')
plt.show()




