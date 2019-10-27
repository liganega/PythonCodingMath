import numpy as np

x = np.arange(-5,6)
y = np.arange(-5,6)

for i in range(len(x)):
    for j in range(len(y)):
        if (-3*x[i] - 2*y[j] < 4) and (x[i] + 5*y[j] > -11):
            print (x[i], y[j])
