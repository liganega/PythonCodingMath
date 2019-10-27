import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2,11)
y = x + np.sqrt(x-2)
plt.plot(x,y)