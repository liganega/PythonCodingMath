import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

def factorization(a): # 약수 구하기
    b = range(1, a)   
    factors = []
    for i in b:
        if a % i == 0:
            factors.append(i)
    factors.append(a)
    return factors

x = np.arange(1,101)
y = []
for i in x:
    factors = factorization(i)
    len_factors = len(factors)
    y.append(len_factors)
plt.plot(x,y)
plt.grid()