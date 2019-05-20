# -*- coding: utf-8

"""
  Code to solve a system of equations
"""

import numpy as np
import time
np.set_printoptions(threshold=1e10)

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
	S = end-start
	
	return np.array(x),S


def numpy_solver(A,b):
	
	#To track the time involved
	start = time.time()
	
	x = np.linalg.solve(A, b)
	
	end = time.time()
	S = end-start
	
	return x,S


#--------------------------------------------------------------------

c=1
A = np.loadtxt('LSE1_A.dat')*c
b = np.loadtxt('LSE1_b.dat')*c

det = np.linalg.det(A)
sign, log = np.linalg.slogdet(A)
#print('sign and log ',sign,log)
print('determinant via det is ',det/c**len(b))
print('determinant via log is ',sign*np.exp(log)/np.exp(np.log(c**len(b))))
 
x1, s1 = gaussian_elimination(A,b)
x2, s2 = numpy_solver(A,b)

print('\nSolutions: \n{}\n'.format(x1,x2))
#To verify if the vector is the answer
#print(np.allclose(np.dot(A, x1), b))

#print times with gauss and numpy
print('\nThe timing using Gauss was  {} s'.format(s1))
print('The timing using Numpy was  {} s'.format(s2))
