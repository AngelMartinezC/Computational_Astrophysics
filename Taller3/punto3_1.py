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


# Define array and the point
X = np.linspace(-1,1,100)
X0 = 0.0

print(' Derivative at ',X0)
print(' Backward  {}'.format(backward(x0=X0)))
print(' Forward   {}'.format(forward(x0=X0)))
print(' Central   {}'.format(central(x0=X0)))


# Plot
def plot(X0=0.2):
	x = np.linspace(-1,1,100)
	plt.plot(x,f(x),linewidth=3,color='b',label='f(x)')
	plt.plot(x,backward(x0=X0)*x + (1-backward(x0=X0))*X0 - np.sin(X0),label='backward')
	plt.plot(x,forward(x0=X0)*x + (1-forward(x0=X0))*X0 - np.sin(X0),label='forward')
	plt.plot(x,central(x0=X0)*x + (1-central(x0=X0))*X0 - np.sin(X0),label='central')
	plt.xlim((-1.0,1.0))
	plt.ylim((-0.15,0.15))
	plt.legend()
	plt.show()
#plot(0.5)
