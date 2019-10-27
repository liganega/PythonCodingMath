from fractions import Fraction  

def prime_factorization(a):
    b = range(2,a)
    primes = []
    for i in b:   # b의 요소인 i에 대해
        while a % i == 0: # a를 로 나누어서 나머지가 0이면
            primes.append(i) # c에 i를 추가하고
            a /= i   # a를 i로 나눈다음
    if primes == []:
        primes.append(a)
    return primes

def finite_OX(a,b):
    finite = True
    primes = prime_factorization(Fraction(a,b).denominator)
    for i in primes:
        if i != 2 and i != 5:    # i가 2가 아니고 5도 아니면
            finite = False       # finite은 거짓
    return finite

print (finite_OX(17,30))
print (finite_OX(12,15))