import numpy as np

a = []
x = np.arange(1,31)
discount = 6000*30*(1-0.7)
print ('30명이 할인받은 금액은 {}원'.format(discount))
for i in x:
    if i*6000 <= discount:
        a.append(i)
print(a)
print ('{}명 일때 단체권 사는게 유리하다.'.format(max(a)))
