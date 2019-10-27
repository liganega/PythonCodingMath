import numpy as np

x = [9,3,5,2,7,2,6,6,7,7,8,8,10]
print (np.bincount(x).argmax())
