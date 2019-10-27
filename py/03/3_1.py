import numpy as np
from fractions import Fraction

plus_5 = lambda x: x+5 
print (plus_5(7))
print (plus_5(np.array([1,2,3,4,5])))

a = lambda x, y: x+y
print (a(2,6))