
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

height = [3,4,5,9,7,2]
bin = np.array([145,150,155,160,165,170]) + 2.5
plt.bar(bin, height, width = 4)
plt.grid()

print ((3+4+5) / (sum(height)) * 100)