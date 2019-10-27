def complement(a,b):
    c = a + []
    for i in b:   
        if i in a: 
            c.remove(i) 
    c.sort()
    return c

a = [1,3,4,5,6]
b = [2,4,6,3,0]

c = complement(a,b)
d = complement(b,a)
print ('a - b = {}'.format(c))
print ('b - a = {}'.format(d))