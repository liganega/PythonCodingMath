import numpy as np

n = 1
for i in range(5):
    temp = np.random.randint(1,10)
    print (temp)
    n *= temp
print (n)