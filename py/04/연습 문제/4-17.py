import numpy as np
import matplotlib.pyplot as plt

a = np.arange(-10,0)
b = np.arange(-10,1)

x = np.arange(-10,11)
y1 = -3/4*x + 3

plt.plot(x, y1)
for i in a:
    y2 = -2*x - i
    plt.plot(x,y2, label = 'a = {}'.format(i))
plt.grid()
plt.legend(fontsize = 14, loc = 3)


x = np.arange(-10,11)
y1 = -3/4*x + 3
plt.figure()
plt.plot(x, y1)
for i in a:
    y2 = -2*x - i
    plt.plot(x,y2, label = 'a = {}'.format(i))
plt.grid()
plt.legend(fontsize = 14, loc = 1)
plt.xlim([0,7])
plt.ylim([0,10])