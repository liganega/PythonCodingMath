import numpy as np

x = [0, 1, 3, 6, 12, 13, 10, 7, 5, 1]
mean = np.average(x)
print(mean)
variance = 0
for i in range(len(x)):
    variance += (x[i]-mean)**2
variance /= len(x)
std = np.sqrt(variance)

print ('분산 : {}'.format(variance))
print ('표준편차 : {}'.format(std))
print (np.var(x))
print (np.std(x))