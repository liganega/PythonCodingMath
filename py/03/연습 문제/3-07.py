import numpy as np

a = np.array(range(1,25))
b = a.reshape(6,4)
for i in range(6):
    for j in range(4):
        b[i,j] = (b[i,j]*i) + j
print (b)