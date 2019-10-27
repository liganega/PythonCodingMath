import numpy as np

x = np.arange(-10,11)
b = list(filter(lambda a: a + 5 >= 4, x))
print (b)

y = list(filter(lambda a: a - -4 <= -3,  np.arange(-10,11,1)))
print (y)

y = list(filter(lambda a: 2/3*a >= -4,  np.arange(-10,11,1)))
print (y)

a = []
for i in x:
    if i + 5 >= 4:
        a.append(i)
print (a)