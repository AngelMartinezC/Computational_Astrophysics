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
	#y= 3*x**5 + 5*x**4-x**3
	y = x**12-2.72071*x**11-231.563*x**10+626.272*x**9+17078.7*x**8-\
		41646*x**7-423658*x**6+651721*x**5+3.20216e6*x**4-\
		2.95117e6*x**3-6.04444e6*x**2+3.79926e6*x+1.79029e6
	y = 1e-2*(x-10)*1e-2*(x-9)*1e-2*(x+10)*(x+1.5)*(x-1.5)*(x-np.pi)*(x+0.333)*(x+np.pi**2)*(x+np.exp(1))*(x-1)*(x+4.5)*(x-7)*x*(x-1e-1)*1e-1*(x+7.7)*(x-8)*1e-4*(x-3.8)*0.0001*(x-0.001)*(x-6.6)
	y = (x-1)*(x-1.9)*(x-1.5)*(x-2)*(x-0.1)*x**2
	y = (x-2)*(x-1)*(x+1)*(x+2)*x**2
	#y=np.sinc(10*x)
	#y=(x-2)*(x+3)*(x-5)
	y=(x+10)*(x-0.001)**2*x**2
	return y


def x(E,a=1.496e8):
	return a*np.cos(E)

def y(E,e):
	b=a*mp.sqrt(1-e**2)
	return b*np.sin(E)




solution=[]
def iteration(f,a,b,epsilon=1e-10,i=0,**kwargs):
	
	i=i+1
	c=(a+b)/2
	A=f(x=a,**kwargs)
	B=f(x=b,**kwargs)
	C=f(x=c,**kwargs)
	print()
	print(i,a,b,c)
	print(i,A,B,C)
	if C==0 or (abs((C-A)/A)< epsilon) or (abs((C-B)/B) < epsilon) or abs(C)<=1e-160:
		print(' ...Appending root')
		
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
	
	if A*B > 0:
		B = -B
	
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
	
	if A==0:
		solution.append(a)
		print(' ...Appending root')
	
	if B==0:
		solution.append(b)
		print(' ...Appending root')
			
			
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
		i=0
		print('values is {} '.format(values))
		for j in values:
			SOL = iteration(f,a=j[0],b=j[1],epsilon=epsilon,i=i,**kwargs)
			if isinstance(SOL[0],(int,float)):
				i = SOL[1]
				solution.append(SOL[0])

	return solution




if __name__=='__main__':

	time = 365.2563
	eccentricity = 0.99999
	a = -0.1
	b = 0.7
	
	print('Almost general method to find all roots in an interval\n')
	SOLUTION=bisection(f,a=a,b=b,e=eccentricity,w=2*np.pi/365.25635,t=time,epsilon=1e-22)
	SOLUTION.sort()
	j=0
	for i in SOLUTION:
		j=j+1
	print('\nThere are {} real roots of the function on [{}:{}]\n Roots:  {}'.format(j,a,b,SOLUTION))


	x = np.linspace(a,b,10000)
	plt.plot(x,f(x))
	plt.axhline(y=0,color = 'r')
	plt.show()


