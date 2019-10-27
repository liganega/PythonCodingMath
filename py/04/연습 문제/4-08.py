import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

x = np.arange(-10,10)
plt.plot(x, x+5)
plt.plot(x, -2*x+7)
plt.grid()
plt.axhline(y = 0)

a = 0,1,0
b = 1,-1, -5
c = 2, 1, 7
x1, y1 = simultaneous_eq(a,b)
x2, y2 = simultaneous_eq(b,c)
x3, y3 = simultaneous_eq(c,a)

area = y2*(x3-x1)/2
print (x1,y1)
print (x2,y2)
print (x3,y3)
print ('삼각형의 넓이는 {}'.format(float(area)))