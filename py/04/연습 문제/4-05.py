import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

x = np.arange(-10,11)
y = np.zeros(len(x))
for i in range(len(x)):
    if x[i] >= 0:
        y[i] = x[i]
plt.plot(x,y)
plt.grid()