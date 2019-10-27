import numpy as np

x = -3
y = -1/2
A = x**2 + 3*y
B = -x - 4*y**2
print (A + B)

x = range(-5,6,1)
y = range(-5,6,1)
A_plus_B = np.zeros((len(x), len(y)))
for i in range(len(x)):
    for j in range(len(y)):
        A = x[i]**2 + 3*y[j]
        B = -x[i] - 4*y[j]**2
        A_plus_B[i,j] = A + B
print('A+B의 크기는 {}'.format(A_plus_B.shape))
print (A_plus_B)
print ('')

print (np.max(A_plus_B))
print (np.min(A_plus_B))
print (np.where (np.max(A_plus_B) == A_plus_B))
print ('')
print (A_plus_B[0,5])
print ('')

print (np.where (np.min(A_plus_B) == A_plus_B))
print (A_plus_B[5,0], A_plus_B[6,0])