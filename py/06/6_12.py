import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,6)
y = x**2
plt.plot(x,y)
plt.grid()

y2 = 2*x**2
y3 = 0.5*x**2
plt.figure()
plt.plot(x,y3, label = 'a = 0.5')
plt.plot(x,y, label = 'a = 1')
plt.plot(x,y2, label = 'a = 2')
plt.legend(fontsize = 14)
plt.grid()

y2 = 2*x**2
y3 = 0.5*x**2
plt.figure()
plt.plot(x,-y3, label = 'a = -0.5')
plt.plot(x,-y, label = 'a = -1')
plt.plot(x,-y2, label = 'a = -2')
plt.legend(fontsize = 14)
plt.grid()