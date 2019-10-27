import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

x = 1
y = 2
plt.scatter(x,y)


x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.figure()
plt.scatter(x,y)

plt.figure()
plt.scatter(x,y, s = 100)

plt.figure()
plt.scatter(x,y, s = 100, c = 'g')

plt.figure()
plt.scatter(x,y, s = 100, c = 'g', alpha = 0.5)