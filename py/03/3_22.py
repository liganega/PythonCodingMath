import numpy as np

x1 = list(filter(lambda a: -4 < a,  np.arange(-10,11,1)))
x2 = list(filter(lambda a: 5*a + 1 <= 4*a + 3,  np.arange(-10,11,1)))

print (x1)
print (x2)

def intersection(a,b):
    c = []
    for i in a:
        if i  in b:
            c.append(i)
    return c

print (intersection(x1, x2))

