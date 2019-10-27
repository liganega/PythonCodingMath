import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

x = np.arange(-5,11)
y = 3*x + 2
y2 = 3*x + 2 + 5
plt.plot(x,y, label = 'original')
plt.plot(x, y2, label = 'y : 5')
plt.legend(fontsize = 14)
plt.grid()