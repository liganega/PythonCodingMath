a = 17
a_prime = True                  # True는 '참'이라는 의미이며 초기값을 참으로 정의
for i in range(2,a):            # 2부터 자기자신 -1까지의 수에대해
    if a % i == 0:              # a를 i로 나눈 나머지가 0이면, 
        a_prime = False         # a_prime을 '거짓'의 의미인 False로 바꾸어라

if a_prime == True:
    print ('{}는 소수이다.'.format(a))  # 소수이다를 출력하라
else:
    print ('{}는 소수가 아니다.'.format(a))
    
def is_prime(a):
    b = range(2, a)  #2부터 a-1까지의 list
    c = 0
    for i in b:    
        if a % i == 0:  
            c += 1   
    if c > 0:
        print ('{}는 소수가 아니다.'.format(a))
        d = False   
    else:
        print ('{}는 소수이다.'.format(a))      
        d = True
    return d

print (is_prime(31))
print (is_prime(18))
print (is_prime(597))
print (is_prime(449))