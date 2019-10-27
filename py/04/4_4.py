import numpy as np

def plus(a,b):
    return a+b

print (plus(4,9))
print ('')

print (plus(4,9,1))

def plus(*args):
    return np.sum(np.array(args))

print (plus(3,6,9))
print (plus(3,1,5,6,4,7))
print ('')

def plus_multiple(a,*b):
    return a*np.sum(np.array(b))

print (plus_multiple(3,6,9))
print (plus_multiple(3,1,5,6,4,7))
print ('')

def plus_multiple(a,*b):
    n = len(b)
    for i in range(n):
        print (b[i])
    return a*np.sum(np.array(b))
print (plus_multiple(3,1,5,6,4,7))

def plus(*args):
    print (np.sum(np.array(args)))
plus(3,6,9)