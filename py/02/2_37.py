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

print (float(Fraction(1,4)))

a = Fraction(1,4)
print (prime_factorization(a.denominator))
print ('')


a = Fraction(7,9)
print (prime_factorization(a.denominator))
print (float(a))

