import numpy as np

x = [2,3,5,7]
a = []
for i in x:
    if 3*i + 2 <= 11:
        a.append(True)
    else:
        a.append(False)
print (a)

x = [2,3,5,7]
a = [3*i + 2 <= 11 for i in x]   #x의 원소인 i에 대해 3*1 + 2 <=11 인지 판별하라
print (a)

x = [2,3,5,7]
a = [i for i in x if 3*i + 2 <= 11 ]   #x의 원소인 i에 대해 3*1 + 2 <=11 인지 판별하라
print (a)
print ('')

x = [2,3,5,7]
a = [i for i in x if 4*i -5 > 13]
print (a)
a = [i for i in x if 2*i + 1 < 15]
print (a)

x = np.arange(-10,11)
b = lambda a: a + 5 >= 4
print (b(x))