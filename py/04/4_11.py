import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

a = 2
x = np.arange(-10,10,1)
t = np.arange(-5, 6, 2)
plt.figure(figsize = (5,5))
for i in t:
    plt.plot(x, a*(x-i), label = 'shift {}'.format(i))
plt.grid()
plt.legend()