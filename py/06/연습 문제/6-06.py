import numpy as np
import matplotlib.pyplot as plt

x = [0.5]
n = 100
for i in range(n):
    x.append(3*x[-1]*(1-x[-1]))
plt.plot(range(n), x[:-1])