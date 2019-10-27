a = [1,3,4,5,6] 
b = [2,4,6,3,0]

c = complement(a,b) + complement(b,a) + intersection(a,b) 
c.sort()
print (c)