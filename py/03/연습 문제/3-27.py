import numpy as np

def intersection(a,b):
    c = []
    for i in a:
        if i  in b:
            c.append(i)
    return c

x1 = list(filter(lambda a: 2*a - 3 < 11,  np.arange(-10,11,1)))
x2 = list(filter(lambda a: 3*a - 6 > 9,  np.arange(-10,11,1)))

print (intersection(x1,x2))
