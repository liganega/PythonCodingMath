import numpy as np

x = [9,3,5,2,7,2,6,6,7,7,8,8,10]
frequency = {}
max_n = 0
for i in x:
    frequency[i] = x.count(i)  # 일단 숫자별로 count를 합니다.

for j in frequency:
    print (j,frequency[j])
    if frequency[j] > max_n:
        max_n = frequency[j]
        max_key = j
print ('최빈수는 {}'.format(max_key))
print (np.bincount(x))
print (np.bincount(x).argmax())