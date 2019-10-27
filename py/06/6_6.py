
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-5,6,1)
y = x**2 - 3*x - 7
for i in x:
    print ('x = {}, y = {}'.format(i, i**2 - 3*i - 7))
plt.plot(x, y)
plt.grid()

x = np.arange(-1.6,-1.5,0.01)
y = x**2 - 3*x - 7

plt.figure()
plt.plot(x, y)
plt.grid()

plt.figure()
x = np.arange(4.4,4.7,0.01)
y = x**2 - 3*x - 7
plt.plot(x, y)
plt.grid()