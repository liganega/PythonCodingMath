a = 325
digit_10 = []
while a // 10 != 0:       # a를 10으로 나눠서 몫이 0이 아닐때까지
    e = a % 10            # e는 325를 10으로 나눈 나머지인 5
    digit_10.append(e)    # 5를 d에 추가한다.
    a //= 10              # 325를 10으로 나눈 몫 32를 새로운 a로 정의
                          # 위 과정을 32에 대해서 하고, 또 3에 대해서 한다.
digit_10.append(a)        # 3을 10으로 나눈 나머지인 3을 최종 추가해준다. 
print (digit_10)
digit_10.reverse()        # 순서를 거꾸로 하기
print (digit_10)

def digit_expand(a, n):   # n은 진수를 의미합니다. 10진수면 n에 10을 넣으면 됩니다.
    digit_10 = []
    while a // n != 0: 
        e = a % n  
        digit_10.append(e)
        a //= n 

    digit_10.append(a)
    digit_10.reverse()
    
    return digit_10

a = digit_expand(1732, 10)
print (a)
print ('')

a = digit_expand(11, 2)
print (a)
print ('')

print (digit_expand(1732,2))
print ('')

print (digit_expand(1732,7))
print (digit_expand(1732,9))
print (digit_expand(1732,16))