import numpy as np

a = [1,2,3,4,5]   # list a를 만들어서
b = np.array(a)   # array 자료형으로 바꾸자

print(b)
print (type(b))

print (b[0], b[-5])
print (b[1], b[-4])
print (b[2], b[-3])
print (b[3], b[-2])
print (b[4], b[-1])
print (' ')

print (b[1:3])
print (b[::2])
print (' ')

a+5

c = b + 5
print(b)
print(c)
print (' ')

print (a*2)
print (b*2)

c = b/4
c

c = b**2
c
print (' ')

c = b/4
print (c)
print (' ')

c = b**2
print (c)
print (' ')

d = np.sqrt(c)
print(b)
print(c)
print(d)
