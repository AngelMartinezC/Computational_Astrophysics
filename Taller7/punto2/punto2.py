#-*- coding: utf-8 -*-

"""
 Program to calculate the root plt
"""

import bisection as bis
import numpy as np
import matplotlib.pyplot as plt


# Function to calculate the roots on a given interval

def f(x):
	y = 3*x**5 + 5*x**4 - x**3
	return y


a1 = -10
b1 = 10

SOL=bis.bisection(f,a=a1,b=b1,epsilon=1e-22)

print('The roots of the function on [{}:{}] are {}'.format(a1,b1,SOL[0]))
