def intersection(a,b):
    c = []               
    for i in a:
        if i  in b:
            c.append(i)
    c.sort()
    return c

def factorization(a):
    b = range(1, a)   
    factors = []
    for i in b:
        if a % i == 0:
            factors.append(i)
    factors.append(a)
    return factors

def greatest_common_factor(a, b, show = False):  
    c = factorization(a)         # a의 약수를 구해 c 라는 list에 저장한다. 
    d = factorization(b)         # b의 약수를 구해 d 라는 list에 저장한다. 
    if show:                     # show 가 true이면
        print (c)                # a의 약수인 c를 출력하고
        print (d)                # b의 약수인 d를 출력하고
    e = intersection(c,d)        # c와 d의 교집합을 구한다.
    return max(e)                # 최대값을 return 한다.

def least_common_multiple(a, b):
    c = prime_factorization(a)  # a의 소인수를 구해 c 라는 list에 저장한다. 
    d = prime_factorization(b)  # b의 소인수를 구해 d 라는 list에 저장한다. 
    for i in c:            
        if i in d:              # c와 d의 공통원소이면
            d.remove(i)         # 1개만 취한다.
    e = c + d                   # a, b의 소인수들의 합집합인 소인수분대를 구한다. (공통된것은 1번만 계산)
    f = 1
    for i in e:     # e의 모든 원소에 대해
        f *= i      # f에다가 계속 곱해라
    return f

print (factorization(60))

factors = factorization(60)[6:]
print (factors)

for i in factors:
    for j in factors:
        if j != i:
            if greatest_common_factor(i, j) == 6:
                if least_common_multiple(i, j) == 60:
                    print ('그 수는 {}와 {}'.format(i,j))