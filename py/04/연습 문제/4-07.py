import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

x = np.arange(-10, 10)
y = 3*x + 5
z = -2*y - 10
#z = -2*(3(x + 5)) - 10
#z = -6*x -10 -10
plt.plot(x,z)
plt.grid()