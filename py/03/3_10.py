import numpy as np

b = [3,4,5,6,7]
print (b.index(6))

c = np.array(b)
c.index(6)

print (np.where(6 == c))
print (np.where(6 == c)[0])
print (np.where(6 == c)[0][0])

a = np.array([3,4,5,7,3,1,3])
print (np.where(3 == a))