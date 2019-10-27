import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

weight = 22, 24, 26, 30, 32, 40, 35, 45, 20, 29, 34, 36, 36, 38, 39, 48, 43, 37, 33, 31, 29, 39, 26, 29
height = [124, 125, 128, 130, 134, 140, 131, 143, 122, 129, 136, 139, 141, 135, 142, 150, 149, 141, 127, 131, 130, 125, 135, 126]

bins = np.arange(20,55,5)  # 도수분포구간

plt.hist(weight, bins)
plt.xlabel('Weight (kg)', fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)

plt.figure()
plt.hist(weight, bins, rwidth = 0.8)
plt.xlabel('Weight (kg)', fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)


plt.figure()
plt.hist(weight, bins, rwidth = 0.8, color = 'green')
plt.xlabel('Weight (kg)', fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)

plt.figure()
plt.hist(weight, bins, rwidth = 0.8, color = 'green', alpha = 0.5)
plt.grid()
plt.xlabel('Weight (kg)', fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)

plt.figure()

plt.bar(b.index, hist, width = 4)
plt.grid()

weight2 = 42, 43, 46, 50, 48, 40, 38, 46, 50, 52, 54, 58, 46, 48, 51, 52, 56, 60, 39, 61, 52, 45, 44, 45

bins2 = np.arange(20,65,5)  # 도수분포 구간
hist2, bin_edges = np.histogram(weight2, bins2)
print (hist2)

plt.figure()
plt.hist(weight2, bins2, rwidth = 0.8, color = 'red', alpha = 0.5)
plt.grid()
plt.xlabel('Weight (kg)', fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)

plt.figure()
plt.hist(weight, bins, rwidth = 0.8, color = 'green', alpha = 0.5, label = '2nd')
plt.hist(weight2, bins2, rwidth = 0.8, color = 'red', alpha = 0.5, label = '4th')
plt.grid()
plt.xlabel('Weight (kg)', fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.legend(fontsize = 14)
plt.ylim([0,9])

print (bins)

size_bins = (bins[1]-bins[0])/2
bins_mean = bins[:-1]+size_bins
print(bins_mean)
accumul_weight = []
previous = 0
for i in hist:
    previous += i
    accumul_weight.append(previous)
print(accumul_weight)

plt.figure()
plt.scatter(bins_mean, accumul_weight)


bins_average = np.multiply(np.array(hist), np.array(bins_mean))
print(bins_average)
average = sum(bins_average)/total_number
print(average)
print (np.mean(weight))