def is_prime2(a):
    b = range(2, a)  #2부터 a-1까지의 list
    c = 0
    for i in b:    
        if a % i == 0:  
            c += 1   
    if c > 0:
        d = False   
    else:
        d = True
    return d

a = range(1,101)              # 100 까지니 101로 지정
prime_numbers = []            # 소수 list를 공집합으로 우선 만들고
for i in a:                   # 1부터 100까지 중,
    c = is_prime2(i)          # i가 소수이면 c는 True, 아니면 False 생성
    if c == True:             # c가 True이면
        prime_numbers.append(i)  # b에다가 i를 추가하라
print (prime_numbers)