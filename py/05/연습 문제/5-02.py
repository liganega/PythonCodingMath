import itertools
import numpy as np


def factorization(a):
    b = range(1, a)   
    factors = []
    for i in b:
        if a % i == 0:
            factors.append(i)
    factors.append(a)
    return factors

complete_number = []
for i in np.arange(1,2001):
    factors = factorization(i)
    del factors[-1]
    if sum(factors) == i:
        complete_number.append(i)
print (complete_number)