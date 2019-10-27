import pandas as pd
import numpy as np

weight = 22, 24, 26, 30, 32, 40, 35, 45, 20, 29, 34, 36, 36, 38, 39, 48, 43, 37, 33, 31, 29, 39, 26, 29

bins = np.arange(20,55,5)  # 도수분포 구간
hist, bins = np.histogram(weight, bins)
print (hist)
print (bins)
print ('')

total_number = len(weight)

hist_normal = np.asarray(hist)/total_number
print(hist_normal)

sum_hist_normal = sum(hist_normal)
print (sum_hist_normal)

accumul_weight = []
previous = 0
for i in hist:
    previous += i
    accumul_weight.append(previous)
print(accumul_weight)