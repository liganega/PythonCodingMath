a = [2,2,2,5]
new_number = []
for i in a:
    if i not in new_number:
        new_number.append(i)
print (new_number)

how_many = []
for j in new_number:
    how_many.append(a.count(j))
print (how_many)

min_n = []
for idx, val in enumerate(how_many):
    if val % 2 == 0:
        min_n.append(1)
    else:
        min_n.append(new_number[idx])
print (min_n)

min_n_multiply = 1
for i in min_n:
    min_n_multiply *= i
print (min_n_multiply)
print ('')

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

def min_n_for_rational(n):
    primes = prime_factorization(n)
    new_number = []
    for i in primes:
        if i not in new_number:
            new_number.append(i)
    print ('소인수분해 : {}'.format(primes))
    print ('소인수 : {}'.format(new_number))
    
    how_many = []
    for j in new_number:
        how_many.append(primes.count(j))
    print ('몇개씩 있나 : {}'.format(how_many))
    
    min_n = []
    for idx, val in enumerate(how_many):
        if val % 2 == 0:
            min_n.append(1)
        else:
            min_n.append(new_number[idx])
    min_n
    print ('얼마나 곱해야 하나 : {}'.format(min_n))
    
    min_n_multiply = 1
    for i in min_n:
        min_n_multiply *= i
    
    print ('{}에서 최소 {}을 곱하면 {}이고 이의 제곱근은 {}이다.'.format(n, min_n_multiply, n*min_n_multiply, np.sqrt(n*min_n_multiply)))

    return min_n_multiply

print (min_n_for_rational(104))
print (min_n_for_rational(105))