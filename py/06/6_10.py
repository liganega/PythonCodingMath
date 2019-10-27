def factorization(a):
    b = range(1, a)
    c = []
    for i in b:
        if a % i ==0:
            c.append(i)
    c.append(a)
    return c

def decomposition(a,b,c):
    if c == 0:
        print ('x({}x+{})'.format(a, b))
    else:
        a_factor = factorization(a)
        c_factor = factorization(c)
        a_minus = list(map(lambda x: x*-1, a_factor))
        c_minus = list(map(lambda x: x*-1, c_factor))
        a_factor += a_minus
        c_factor += c_minus
        for d in a_factor:
            for e in c_factor:
                f = a/d
                g = c/e
                if d*g + e*f == b:
                    if d > 0 or e > 0:
                        print ('{}x^2 + {}x + {} = ({}x +{})({}x+{})'.format(a,b,c,d,e,f,g))
                        break


decomposition(1,4,3)
decomposition(1,-3,2)
decomposition(3,-3,0)
decomposition(1,0,-1)