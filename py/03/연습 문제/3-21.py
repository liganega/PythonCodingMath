import numpy as np
from fractions import Fraction

def simultaneous_eq(a,b):
    if (a[0]/b[0]) == (a[1]/b[1]) != (a[2]/b[2]):
        print ('해는 없다')
        return None, None
    elif (a[0]/b[0]) == (a[1]/b[1]) == (a[2]/b[2]):
        print ('해는 무수히 많다')
        return None, None
    else:
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
    
a = [1,1,60]
b = [1,-2,12]
x, y = simultaneous_eq(a,b)
print (x)