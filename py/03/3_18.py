import numpy as np

a = [5,2,14]
b = [2,1,4]

c = [[5,2], [2,1]]
d = [14,4]
result = np.linalg.solve(c,d)
print (result)

c = [[5,2,1], [2,-3,-4], [1,5,-2]]
d = [14,4,21]
result = np.linalg.solve(c,d)
print (result)