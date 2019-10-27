a = [1,3,4,5,6]
b = [2,4,6,3,0]

for i in a:    
    if i in b:    
        a.remove(i)   
c = a + b
print (c)