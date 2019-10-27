import numpy as np
import matplotlib.pyplot as plt

x = np.arange(6)
y = 2*(x-3)**2 + 4
plt.plot(x,y)
plt.scatter(3,4, s = 100, color = 'r')
plt.grid()