import numpy as np

c = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print (c)

print (c.shape)
print (c[0,0], c[0,1], c[1,0], c[3,2], c[-1,0], c[0,-1], c[-1,-1])
print ('')

print (c[:,0])
print (c[:,4])
print (c[0,:])
print (c[2,:])
print ('')

print (c[:])
print ('')

print (c[1:3, 2:4])
print ('')

c = range(1,26)    # range로 1부터 25까지를 만들고
c = np.array(c)    # numpy의 array자료형으로 바꾼다음
print (c.shape)    # 25 크기의 1차원 배열이 만들어지고
print (c)
print (c.reshape(5,5))     # 이를 5,5형태로 바꾸면