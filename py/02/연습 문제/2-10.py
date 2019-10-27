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

factors = factorization(210)
for i in factors:
    if greatest_common_factor(i, 42) == 6:
        print ('그 수는 {}'.format(i))