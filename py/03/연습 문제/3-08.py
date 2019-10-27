import numpy as np

def triangle_area(a,h):
    return 1/2*a*h

a = 3
h = 5
print (triangle_area(a,h))

a = np.array(range(1,11))
h = np.array(range(1,11))
area = np.zeros((len(a), len(h)))
print (area.shape)

for i in a:
    for j in h:
        area[i-1,j-1] = triangle_area(i,j)
print (area)