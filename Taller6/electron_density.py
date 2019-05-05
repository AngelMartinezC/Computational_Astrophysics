#-*- coding: utf-8 -*-

"""
 Program to calculate integral
"""

import numpy as np
import matplotlib.pyplot as plt
from newton_cotes import integral

#--------------------------------------------------
# Punto a

# Function to calculate the integral
def f(x,kT=20):
	#k = 8.6e-11 # MeV
	#T = 1e9 # K
	# kT in Mev
	hc = 197.3269e-15 # MeV m
	ne = (8*np.pi)*(kT)**3/(2*np.pi*hc)**3*(x**2/(np.exp(x)+1))
	return ne

#x = np.linspace(0,20,1000)
#plt.plot(x,f(x),label=r'$dn_{e^\pm}=\frac{(8\pi k_BT)^3}{(2\pi \hbar c)^2} \frac{x^2}{e^x +1}$')
#plt.legend()
#plt.show()

# The function f(x) goes to zero after x=10, so the integral is made up to 20
A = integral(f,a=0,b=20,N=100,method='simpson')
B = integral(f,a=0,b=20,N=10000,method='simpson')
print(' Electronic/positronic density is    ne : {}'.format(A))
print(' Electronic/positronic density is    ne : {}'.format(B))



#--------------------------------------------------
# Punto b

def ne(x,kT=20):
	# Energy units in Mev (to make the step also in Mev)
	hc = 197.3269e-15 # MeV m
	beta = 1/kT
	return 8*np.pi/(2*np.pi*hc)**3*(x**2/(np.exp(beta*x)+1))

# Define Delta E
DE = 5
E = np.arange(0,300,DE)  # Negigle up to 300

# Create ne/DE
nei, Ei = [], []
for i in E:
	Eold = i
	Enew = i+DE
	Eix = (Enew+Eold)/2
	nei.append(ne(Eix)/DE)
	Ei.append(Eix)

#plt.plot(Ei,nei)
#plt.show()

# Confirmation
den = 0
for i in nei:
	den += i*DE

print('\n Electronic density with  DE={}  is   ne : {}'.format(DE,den))








