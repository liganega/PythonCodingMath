import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

x = np.arange(0,21)
a = np.random.randint(low = -5, high = 5, size = len(x))
y = x + a
plt.plot(x, y)