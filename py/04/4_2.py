import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

t1 = (1,2,3)
t2 = (4,5,6)
print (t1 + t2)
print (t1 * 2 + t2 * 3)
print ('')

a = np.array([1,2,3,4,5])
b = np.where(a == 3)
print (b)
print (type(b))
print (b[0])
print (type(b[0]))
print (b[0][0])