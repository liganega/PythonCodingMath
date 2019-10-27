import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

plt.scatter((1,2,3,4,5), (1,2,1.3, 3.75, 2.25))

a = np.arange(0, 5, 0.1)
b = np.arange(0, 5, 0.1)
error = np.zeros((len(a), len(b)))
for i in range(len(a)):
    for j in range(len(b)):
        error[i,j] = (a[i]+b[j]-1)**2 + (2*a[i]+b[j]-2)**2 + (3*a[i]+b[j]-1.3)**2 \
        + (4*a[i]+b[j]-3.75)**2 + (5*a[i]+b[j]-2.25)**2
print (np.where(error == np.min(error)))
print (a[4], b[9])


x = np.arange(0,6,1)
plt.figure()
plt.plot(x, 0.4*x + 0.9, 'r')
plt.scatter((1,2,3,4,5), (1,2,1.3, 3.75, 2.25))