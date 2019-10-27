a = 17
b = range(2,a)               # 2부터 23까지의 수열을 만들고
primes = []                  # 소인수들로 이루어진 list를 만들텐데 우선 공집합으로 시작
for i in b:                  # 2부터 23까지 자연수에 대해 i로 놓고
    while a % i == 0:        # a를 로 나누어서 나머지가 0이면
        primes.append(i)     # c에 i를 추가하고
        a /= i               # a를 i로 나눈다음
                             # 이 과정을 반복해라

if primes == []:             # 만약 아무것도 나누어지지 않으면 
    primes.append(a)         # 소인수는 그 수 자체
    
print (primes)

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

print (prime_factorization(128))
print (prime_factorization(497))
print (prime_factorization(10135867))
print (prime_factorization(17))