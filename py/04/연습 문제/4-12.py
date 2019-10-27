import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

x = np.arange(-20,41)
y = x*9/5 + 32
plt.plot(x,y)
plt.xlabel('Celcius', fontsize = 14)
plt.ylabel('Farenheit', fontsize = 14)
plt.grid()