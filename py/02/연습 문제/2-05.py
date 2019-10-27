a = range(2,1001)                   # 2부터 1000 까지 지정
prime_numbers = [1]                # 소수 list를 1부터 시작하는 list로 만들고
diff = 0                           # 소수와 그다음 소수까지의 차이를 우선 0으로 만들고

for i in a:                        # 2부터 1000까지 중,
    c = is_prime2(i)               # i가 소수이면 c는 True, 아니면 False 생성
    if c == True:                  # c가 True이면
        prime_numbers.append(i)    # b에다가 i를 추가하라
        if prime_numbers[-1] - prime_numbers[-2] > diff:
            diff = prime_numbers[-1] - prime_numbers[-2]
            max_diff_primes = [prime_numbers[-2], prime_numbers[-1]]

print ('소수사이 구간의 최대값 : {}'.format(diff))
print ('최대구간의 소수쌍 : {}'.format(max_diff_primes))