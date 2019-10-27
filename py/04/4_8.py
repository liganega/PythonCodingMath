import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

plt.axvline(x = 5, c = 'r', linewidth = 10)  # x = 5에  빨간선 긋기
plt.axhline(y = 2, c = 'b')  # y = 2에 파란색 수평선 긋기
plt.xlim([0,10])
plt.ylim([0,10])
plt.grid()