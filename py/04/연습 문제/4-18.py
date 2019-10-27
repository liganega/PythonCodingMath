import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

def simultaneous_eq(a,b):
    if a[0] == 0:
        y = Fraction(a[2], a[1])
        x = Fraction(b[2] - b[1]*y, b[0])
    elif a[1] == 0:
        x = Fraction(a[2], a[0])
        y = Fraction(b[2] - b[0]*x, b[1])
    elif b[0] == 0:
        y = Fraction(b[2], b[1])
        x = Fraction(a[2] - a[1]*y, a[0])
    elif b[1] == 0:
        x = Fraction(b[2], b[0])
        y = Fraction(a[2] - a[0]*x, a[1])
    else:
        a = np.array(a)
        b = np.array(b)
        c = b* Fraction(a[0],b[0])
        d = a - c
        y = Fraction(d[2],d[1])
        x = Fraction(a[2]-a[1]*y,a[0])
    return x, y

a = [3, -1, -4]
b = [-1, 1, 1]
print (simultaneous_eq(a,b))