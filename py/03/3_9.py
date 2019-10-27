import numpy as np

print (np.zeros((2 ,4)))
print (np.ones((7, 3)))

a = np.zeros((5,5))                                # (5x5) 크기를 가지는 a라는 변수를 우선 선언
for idx1, val1 in enumerate(range(0,25,5)):
    for idx2, val2 in enumerate(range(1,10,2)):
        a[idx1,idx2] = val1 + val2
print (a)