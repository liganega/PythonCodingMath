import numpy as np


x = 2,6,6,8,8,10
length = len(x)
average = sum(x)/length
print (average)

def average(x):
    return sum(x)/len(x)

print (average(x))

average2 = lambda a:sum(a)/len(a)
print (average2(x))


print (np.average(x))