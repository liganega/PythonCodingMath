def factorization(a):
    b = range(1, a)
    c = []
    for i in b:
        if a % i ==0:
            c.append(i)
    c.append(a)
    return c

a_factor = factorization(6)
c_factor = factorization(21)

print (a_factor)
print (c_factor)

a_minus = list(map(lambda x: x*-1, a_factor))
c_minus = list(map(lambda x: x*-1, c_factor))
a_factor += a_minus
c_factor += c_minus

print (a_factor)
print (c_factor)

for d in a_factor:
    for e in c_factor:
        f = 6/d
        g = 21/e
        if d*g + e*f == 23:
            if d > 0 or e > 0:
                print ('6x^2 + 23x + 21 = ({}x + {})({}x + {})'.format(d,e,f,g))
                break