import numpy as np

a = np.array(range(3,121,3))
b = a.reshape(8,5)
print (b)

c = b.reshape(4,10)
print (c)