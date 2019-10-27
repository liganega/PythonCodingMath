import itertools
import numpy as np

x = np.arange(3,1000,3)
y = np.arange(5, 1000, 5)
z = np.arange(15,1000,15)
total = sum(x) + sum(y) - sum(z)
print(total)