def plus_with_5 (a,b, c = 5):
    return a + b + c
print (plus_with_5(1,2))
print (plus_with_5(1,2,10))
print ('')

def calcul(a,b, c = 5, d = 10, e = 15):
    return a + b - c + d - e
print (calcul (1,2, d = 3, c = 10, e = 0.1))

a = 100
def plus_a(n):
    return n+a
print (plus_a(3))

del a
def plus_a(n):
    a = 100
    return a + n
print (plus_a(3))

print(a)