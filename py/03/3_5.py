a = 3
b = 10

print ((a > 0) and (b > 5))
print (type((a > 0) and (b > 5)))
print ((a > 5) and (b > 5))
print ((a > 5) or (b > 5))

for i in range(2,100):
    if (i%4 == 1) and (i % 5 == 1) and (i % 6) == 1:
        print (i)
print ('')

for i in range(1,31):
    if (i % 2 == 0) or (i % 3 == 0):
        print (i)