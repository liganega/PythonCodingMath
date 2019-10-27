import numpy as np

x = [9,3,5,2,7,2,6,6,7,7,8,8,10]
x.sort()
print (x)

n = len(x)
middle_number = n//2

print ('원소갯수 : {}'.format(n))
print ('중앙은 {} 번째 원소'.format(middle_number))
print ('그래서 중앙값은 {}'.format(x[middle_number]))
print (np.median(x))