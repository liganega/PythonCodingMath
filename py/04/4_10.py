import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

a = 1
x = np.arange(-10,11, 1)
plt.figure(figsize = (5,8))
plt.scatter(x, 1/x)
plt.axvline(x = 0, c = 'k')
plt.axhline(y = 0, c = 'k')
plt.grid()