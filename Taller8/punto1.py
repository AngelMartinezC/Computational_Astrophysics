#

"""
	Read and optimization
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii


data = ascii.read('table1.dat',readme='ReadMe')

s = data['sigma*']
M = data['logM']

plt.plot(s,M,'.')
plt.show()
