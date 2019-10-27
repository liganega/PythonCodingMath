x = range(1,9,1)
y = range(1,5,1)
xy = []
for i in x:
    for j in y:
        if i + 2*j == 8:
            xy.append([i,j])
print (xy)
print (len(xy))