import numpy as np

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


a, b = np.random.randint(10,100,size = 2)
print (a,b)
print (least_common_multiple(a, b))