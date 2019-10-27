import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1,5)
y = 3*(x-1)**2 - 2
plt.plot(x,y)
plt.grid()