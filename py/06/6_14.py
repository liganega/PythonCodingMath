import numpy as np
import matplotlib.pyplot as plt

print (9**2 - (4*-5*2) >= 0)

x = np.arange(-5,6)
y = -5*x**2 + 9*x + 2
plt.plot(x,y)
plt.grid()