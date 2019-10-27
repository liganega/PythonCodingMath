import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

price = 800000000
saving = 4000000-1000000-1000000

n = price / saving
year = n // 12
month = n % 12
print ('총 {}년 {}개월이 걸린다.'.format(year, month))

price = 800000000
saving = np.arange(0, 11000000, 1000000)
n = price / saving
plt.plot(saving, n)
plt.grid()