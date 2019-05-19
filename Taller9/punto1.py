# -*- coding: utf-8

"""
  Code to solve a system of equations
"""

import numpy as np
import time

def gaussian_elimination(A,b):
	
	#To track the time involved
	start = time.time()
	
	for j in range(0,len(b)):
		if A[j][j]==0:
			print('The system of equations has no solution')
			exit()
		for k in range(len(b)):
			if j>k:
				a0 = -1*A[j][k]/A[k][k]
				A[j] = a0*A[k] + A[j]
				b[j] = a0*b[k] + b[j]
	
	#Create empty array to put in the results
	x=[0 for i in range(len(b))]
	
	cont = 0
	for i in range(len(b)-1,0-1,-1):
		cont=0
		if i == len(b)-1:
			xinit = (b[i])/A[i][i]
			x[i] = xinit
		else:
			for j in range(i+1,len(b)-1):
				cont += A[i][j]*x[j]
			xi = (b[i] - cont-A[i][len(b)-1]*xinit)/A[i][i]
			x[i] = xi
	
	end = time.time()
	print('\nThe time involved in calculations was {} s\n'.format(end-start))
	
	return x


c=0.5
A = np.loadtxt('LSE4_A.dat')*c
b = np.loadtxt('LSE4_b.dat')

det = np.linalg.det(A)
sign, log = np.linalg.slogdet(A)
print(det)
print(sign*np.exp(log))
print(log)
print('det is ',sign*np.exp(log)/c**len(b))


x = gaussian_elimination(A,b)
#print(x)







