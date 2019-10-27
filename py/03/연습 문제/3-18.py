from fractions import Fraction
import numpy as np


a = [1,5,20]  # 
b = [Fraction(1,2), Fraction(1,3), 4]
c = b*2
print (c)

a = np.array(a)
b = np.array(b)
c = b*2
print (c)

d = a-c
y = Fraction(d[2], d[1])
x = Fraction((a[2]-a[1]*y),a[0])
print (x, y)

def simultaneous_eq(a,b):
    a = np.array(a)
    b = np.array(b)
    c = b* Fraction(a[0],b[0])
    d = a - c
    y = Fraction(d[2],d[1])
    x = Fraction(a[2]-a[1]*y,a[0])
    return x, y

a = [5,2,14]
b = [2,1,4]
x, y = simultaneous_eq(a,b)
print (x, y)

a = [2, 3, 4]   
b = [3, -4, -4]
x, y = simultaneous_eq(a,b)
print (x, y)