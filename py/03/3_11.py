import numpy as np

a = np.array([-3,4,7,2,5])
print (max(a))
print (min(a))

c = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])

cmax = np.max(c)
print ('최댓값은 : {}'.format(cmax))
cmax_index = np.where(cmax == c)
print ('최댓값 {}의 index는 {}'.format(cmax, cmax_index))