import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

x = np.arange(1,11)
pairs = [(i,i**2) for i in x]
print (pairs)

y = x**2
pairs2 = list(zip(x,y))
print (pairs2)