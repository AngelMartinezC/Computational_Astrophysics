#-*- coding: utf-8 -*-

"""
 Program to calculate the root
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x,e=0.0167,w=2*np.pi/365.25635,t=91):
	y = x - e*np.sin(x)-w*t
	#y = (x**6-14*x**4+49*x**2-36)*x
	#y = np.sin(x)
	y= 3*x**5 + 5*x**4-x**3
	y = (x-10)*(x-9)*(x+10)*(x+1.5)*(x-1.5)*(x-np.pi)*(x+0.333)*(x+np.pi**2)*(x+np.exp(1))*(x-1)*(x+4.5)*(x-7)*x
	return y


def x(E,a=1.496e8):
	return a*np.cos(E)

def y(E,e):
	b=a*mp.sqrt(1-e**2)
	return b*np.sin(E)


def iteration(f,a,b,epsilon=1e-15,i=0,**kwargs):
	while True:
		c=(a+b)/2
		A=f(x=a,**kwargs)
		B=f(x=b,**kwargs)
		C=f(x=(a+b)/2,**kwargs)
		i=i+1
		print('Iteration {}'.format(i))
		if A>B:
			if C>0: a=c
			if C<0: b=c
			if abs(C)<epsilon: break
		elif A<B:
			if C>0: b=c
			if C<0: a=c
			if abs(C)<epsilon: break
	return c,i


def bisection(f,a,b,epsilon=1e-10,sample=500,**kwargs):
	
	c=(a+b)/2
	A=f(x=a,**kwargs)
	B=f(x=b,**kwargs)
	C=f(x=c,**kwargs)
	solution=[]
	
	if a+b ==0:
		C=f(x=c,**kwargs)
		if C==0:
			solution.append(c)
			a=a+0.5
	
	# Make an interval from a to b in order to locate the points near a root
	if A*C >= 0 or A*C<0 or B*C >= 0 or B*C<0:
		XX = np.linspace(a,c,sample)
		YY = np.linspace(c,b,sample)
		values=[]
		for i in range(0,len(XX)-2,2):
			ai, ay = f(x=XX[i],**kwargs), f(x=YY[i],**kwargs)
			bi, by = f(x=XX[i+2],**kwargs), f(x=YY[i+2],**kwargs)
			si = ai*bi
			sy = ay*by
			if si<0:
				values.append([float(XX[i]),float(XX[i+2])])
			if sy<0:
				values.append([float(YY[i]),float(YY[i+2])])
		i=0
		for j in values:
			SOL=iteration(f,a=j[0],b=j[1],epsilon=epsilon,i=i,**kwargs)
			i=SOL[1]
			solution.append(SOL[0])

	if A==0:
		solution.append(a)
		print(' ...Appending root')
		A=f(x=a+0.01,**kwargs)
		a=a+0.01
	
	if B==0:
		solution.append(b)
		print(' ...Appending root')
		B=f(x=b-0.01,**kwargs)
		b=b-0.1*epsilon
	
	if (abs((C-A)/A)< epsilon) or (abs((C-B)/B) < epsilon):
		solution.append(c)

	return solution



if __name__=='__main__':

	time = 365.2563
	eccentricity = 0.99999
	a = -10.1
	b = 10

	SOLUTION=bisection(f,a=a,b=b,e=eccentricity,w=2*np.pi/365.25635,t=time,epsilon=1e-22)
	SOLUTION.sort()
	j=0
	for i in SOLUTION:
		j=j+1
	print('There are {} real roots of the function on [{}:{}]\n Roots:  {}'.format(j,a,b,SOLUTION))


	x = np.linspace(a,b,10000)
	plt.plot(x,f(x))
	plt.show()






