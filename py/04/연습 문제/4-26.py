import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

years = np.arange(0,61,1)

bully = (years-20)*1000
salaryman = (years-27)*3000
doctor = (years-36)*15000

bully[:20] = 0
salaryman[:27] = 0
doctor[:36] = 0

plt.plot(years, bully, label = 'Bully')
plt.plot(years, salaryman, label = 'Salaryman')
plt.plot(years, doctor, label = 'Doctor')
plt.grid()
plt.legend(fontsize = 14)