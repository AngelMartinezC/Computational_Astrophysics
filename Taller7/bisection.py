#-*- coding: utf-8 -*-

"""
 Program to calculate the root
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x,e=0.0167,w=2*np.pi/365.25635,t=91):
	y = x - e*np.sin(x)-w*t
	y = (x-1)*(x-1.9)*(x-1.5)*(x-2)*(x-0.1)*(x+4)
	return y



solution=[]
def iteration(f,a,b,epsilon=1e-10,i=0,**kwargs):
	i=i+1
	c=(a+b)/2
	A=f(x=a,**kwargs)
	B=f(x=b,**kwargs)
	C=f(x=c,**kwargs)
	
	if C==0 or (abs((C-A)/A)< epsilon) or (abs((C-B)/B) < epsilon) or abs(C)<=1e-160:
		#print(' ...Appending root')
		
		if abs(c)<1e-50: #zero value redefinition
			c=0
			return c,i
		else: 
			return float(c),i
	
	if A*C < 0:
		a=a
		b=c
		return iteration(f,a=a,b=c,epsilon=epsilon,i=i,**kwargs)

	if B*C < 0:
		a=c
		b=b
		return iteration(f,a=c,b=b,epsilon=epsilon,i=i,**kwargs)
	
	else: return None,None

"""
print('roots',iteration(f,-1, 11,epsilon=1e-15))
x = np.linspace(-1,11,10000)
plt.plot(x,f(x))
plt.axhline(y=0,color = 'r')
plt.show()
"""

def bisection(f,a,b,epsilon=1e-20,sample=10000,**kwargs):
	
	a,b = float(a),float(b)
	c=(a+b)/2
	A, B =f(x=a,**kwargs), f(x=b,**kwargs)
	C=f(x=c,**kwargs)
	solution=[]
	ite=0
	
	if A==0:
		solution.append(a)
		#print(' ...Appending root')
	
	if B==0:
		solution.append(b)
		#print(' ...Appending root')
			
			
	# Make an interval from a to b in order to locate the points near a root
	if A*C >= 0 or A*C<0 or B*C >= 0 or B*C<0:
		XX = np.linspace(a,b,sample)
		values=[]
		for i in range(1,len(XX)-1,2):
			ai, bi = f(x=XX[i-1],**kwargs), f(x=XX[i+1],**kwargs)
			si = ai*bi
			if si<0:
				values.append([float(XX[i-1]),float(XX[i+1])])
			if si>0:
				ci = f(x=XX[i],**kwargs)
				m1 = (ci-f(x=XX[i-2],**kwargs))/(XX[i]-XX[i-2])
				m2 = (f(x=XX[i+2],**kwargs)-ci)/(XX[i+2]-XX[i])
				if m1*m2 <= 0 :
					values.append([float(XX[i-1]),float(XX[i+1])])
		for j in values:
			ite=0
			SOL = iteration(f,a=j[0],b=j[1],epsilon=epsilon,i=ite,**kwargs)
			if isinstance(SOL[0],(int,float)):
				ite = SOL[1]
				solution.append(SOL[0])

	return solution,SOL[1]




if __name__=='__main__':

	time = 365.2563
	eccentricity = 0.99999
	a = -4
	b = 4
	
	print('Almost general method to find all roots in an interval\n')
	SOLUTION=bisection(f,a=a,b=b,e=eccentricity,w=2*np.pi/365.25635,t=time,epsilon=1e-22)[0]
	SOLUTION.sort()
	j=0
	for i in SOLUTION:
		j=j+1
	print('\nThere are {} real roots of the function on [{}:{}]\n Roots:  {}'.format(j,a,b,SOLUTION))

	x = np.linspace(a,b,10000)
	plt.plot(x,f(x))
	plt.axhline(y=0,color = 'r')
	plt.show()


