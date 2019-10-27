import numpy as np


xy = np.zeros((20,20))

for i in range(1,21):
    for j in range(1,21):
        xy[i-1,j-1] = i*j
print (xy)