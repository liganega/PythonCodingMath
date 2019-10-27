import numpy as np

a = np.arange(-10,0)
b = np.arange(-10,1)
result = []
for i in a:
    for j in b:
        if j == -3 - i:
            result.append((i,j))

print (result)