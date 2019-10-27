print ([i for i in range(-10,11) if 3*i - 7 <= 3])
print (list(filter(lambda i: 3*i -7 <= 3, range(-10,11,1))))

a = []
for i in range(-10,11):
    if 3*i - 7 <= 3:
        a.append(i)

print (a)