
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

x = np.arange(-2, 8)
y = 5*x - x**2
plt.plot(x,y)
plt.grid()

for i in x:
    print ((i, 5*i-i**2))