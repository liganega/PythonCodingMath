import numpy as np

x = np.arange(1,7)
y = np.arange(1,7)

x_minus_y = []
for i in x:
    for j in y:
        x_minus_y.append(i-j)
print (np.var(x_minus_y))