# -*- coding: utf-8

"""
  Code to solve a system of equations
"""

import numpy as np

def gaussian_elimination(A,b):
	
	for j in range(0,len(b)):
		if A[j][j]==0:
			print('The system of equations has no solution')
			exit()
		for k in range(len(b)):
			if j>k:
				a0 = -1*A[j][k]/A[k][k]
				A[j] = a0*A[k] + A[j]
				b[j] = a0*b[k] + b[j]
		
	x3 = (b[2])/A[2][2]
	x2 = (b[1]-A[1][2]*x3)/A[1][1]
	x1 = (b[0]-A[0][1]*x2-A[0][2]*x3)/A[0][0]
	
	x=[0 for i in range(len(b))]
	
	cont = 0
	for i in range(len(b)-1,0-1,-1):
		cont=0
		#print(i,'new\n')
		if i == len(b)-1:
			xinit = (b[i])/A[i][i]
			x[i] = xinit
		else:
			#print(x)
			for j in range(i+1,len(b)-1):
				cont += A[i][j]*x[j]
				
			#	print(i,j,'\n')
			xi = (b[i] - cont-A[i][len(b)-1]*xinit)/A[i][i]
			x[i] = xi
	
	#x = np.array([x1,x2,x3])
	
	return x

A = np.loadtxt('LSE1_A.dat')
b = np.loadtxt('LSE1_b.dat')

x = gaussian_elimination(A,b)

print(x)







