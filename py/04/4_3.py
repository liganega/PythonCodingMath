import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

a = [1,2,3]
b = ['a', 'b','c']
list(zip(a,b))
print (tuple(zip(a,b)))

a = (1,2,3)
b = ['a', 'b','c']
print (list(zip(a,b)))

a = [1,2,3]
b = ['a','b','c']
c = ['딸기', '복숭아', '참외']
d = list(zip(a,b,c))
print (d)