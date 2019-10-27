import numpy as np

a = range(5,35,5)
x = range(5,11,1)
cost = np.zeros((len(a), len(x)))
for i in range(len(a)):
    for j in range(len(x)):
        cost[i,j] = 10000*(1-a[i]/100)*x[j]
print (cost)

print (np.where(np.max(cost) == cost))
print (cost[0,5])