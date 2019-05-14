#

"""
	Read and optimization
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii



def linear(x,y,sigma=None):

	if isinstance(sigma,(list,np.ndarray)):
		s = sigma
		for i in range(len(x)):
			if not isinstance(s[i],(int,float)):
					s[i] = 1
			else: pass
	elif isinstance(sigma,(int,float)):
		s = [sigma for i in range(len(x))]
	elif sigma==None:
		s = [1 for i in range(len(x))]
	else: pass
	#print(s,'\n')

	S,X,Y,X2,XY =0,0,0,0,0
	for i in range(len(s)):
		S  += 1/(s[i]**2)
		X  += x[i]/(s[i]**2)
		X2 += (x[i]**2)/(s[i]**2)
		Y  += y[i]/(s[i]**2)
		XY += x[i]*y[i]/(s[i]**2)

	b = (Y*X2-X*XY)/(S*X2-X**2)
	m = (S*XY-X*Y)/(S*X2-X**2)

	return m, b


def plot(name='table1.dat',readme='ReadMe',fig='Mvssigma_noadd.png'):
	data = ascii.read(name,readme=readme)

	s = data['sigma*']
	logs = np.log10(data['sigma*'])
	logM = data['logM']

	err_s = np.log10(data['e_sigma*'])
	err_M = data['e_logM']
	Err_M = data['E_logM']

	M,   B   = linear(x=logs, y=logM)
	print('M is ',M)
	print('B is ',B)
	print(np.log10(4.02))
	print(np.log10(7.96))
	Mye, Bye = linear(x=logs, y=logM, sigma=err_M)
	MyE, ByE = linear(x=logs, y=logM, sigma=Err_M)

	plt.figure(figsize=(5,5))
	x = np.linspace(1.4,2.65,1000)
	plt.xlim(1.4,2.65)
	plt.ylim(4.5,10)
	plt.xticks([1.5,1.75,2,2.25,2.5])
	plt.yticks([5,6,7,8,9])
	plt.plot(logs,logM,'o',fillstyle='none',markersize=5)
	plt.plot(x,M*x+B,label='linear fit')
	plt.plot(x,Mye*x+Bye,label='low fit y')
	plt.plot(x,MyE*x+ByE,label='high fit y')
	plt.xlabel(r'$\log (\sigma _{\star} / $ km s$^{-1})$')
	plt.ylabel(r'$\log ($ $M_{BH}$ $/$ M$\odot $ $)$')
	plt.legend()
	plt.savefig(fig)
	plt.show()


plot()
plot(name='table2.dat',readme='ReadMe2',fig='Mvssigma.png')

