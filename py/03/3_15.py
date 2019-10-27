x = (5+3)/2
x

x = -10/(3 + 7)
x

def linear_eq(a,b,c):
    x = Fraction((c-b),a)
    return x
linear_eq(2,-3,5)

def linear_eq(a,b,c):
    x = Fraction((c-b),a)
    if x.denominator == 1:
        x = int(Fraction(x))
    return x
linear_eq(2,-3,5)