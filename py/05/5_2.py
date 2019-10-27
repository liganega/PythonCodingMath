import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

weight = 22, 24, 26, 30, 32, 40, 35, 45, 20, 29, 34, 36, 36, 38, 39, 48, 43, 37, 33, 31, 29, 39, 26, 29

hist = np.zeros(6)
for i in weight:
    if i//5 == 4:
        hist[0] += 1
    elif i//5 == 5:
        hist[1] += 1
    elif i//5 == 6:
        hist[2] += 1
    elif i//5 == 7:
        hist[3] += 1
    elif i//5 == 8:
        hist[4] += 1
    elif i//5 == 9:
        hist[5] += 1
print (hist)
print ('') 

index = ['20~25', '25~30', '30~35', '35~40', '40~45', '45~50']
a = pd.Series(hist, index = index)
print (a)
print (type(a))
print ('') 

type(a)

index = np.array([20, 25, 30, 35, 40, 45]) + 2.5
b = pd.Series(hist, index = index)
print (b)
print ('') 

index = np.array([20, 25, 30, 35, 40, 45]) + 2.5
b = pd.Series(hist, index = index, dtype = int)
print (b)
print ('') 

b.name = 'A반의 체중 도수분포표'
print (b)
print ('')

print (a.index)
print (b.index)