a = 24
b = range(1, 24)            # 1부터 23까지 자연수의 집합
factors = []                # 약수 list를 공집합으로 만들어놓고
for i in b:                 # b의 원소 i에 대해
    if a % i == 0:          # 24가 i로 나눈 나머지가 0이면
        factors.append(i)   # 약수집합에 i를 추가하여라
factors.append(a)           # 자기자신인 24를 추가하여라
print (factors)

def factorization(a):
    b = range(1, a)   
    factors = []
    for i in b:
        if a % i == 0:
            factors.append(i)
    factors.append(a)
    return factors

print (factorization(36))
print (factorization(148))