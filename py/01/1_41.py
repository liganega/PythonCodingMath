def intersection(a,b):
    c = []               
    for i in a:
        if i  in b:
            c.append(i)
    c.sort()
    return c

a = [1,3,4,5,6]
b = [2,4,6,3,0]
print (intersection(a,b))

a = [1,3,5,7,9]
b = [2,4,6,8,0]
c = intersection(a,b)
print (c)
