a  = range(5)
print (a)
print (type(a))

b = range(0,5)
print (b)

for i in range(5):
    print (i)
    
b = range(0,5)
print (b)

for i in range(0,9,2):
    print (i)
    
for i in range(0,9,-2):
    print (i)
    
for i in range(0,-9,-2):
    print (i)
    
a = 0
for i in range(0,101):
    a += i
print ('0부터 100까지 더한 값 : {}'.format(a))

a = 0
for i in range(0,101):   # 0부터 100까지 중
    if i % 2 == 1:     # 2로 나누어서 1이면(나머지가 1이면)
        a += i         # a에 더하라.
print ('0부터 100까지 홀수를 더한 값 : {}'.format(a))