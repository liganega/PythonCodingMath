import numpy as np

def digit_expand(a, n):   # n은 진수를 의미합니다. 10진수면 n에 10을 넣으면 됩니다.
    digit_10 = []
    while a // n != 0: 
        e = a % n  
        digit_10.append(e)
        a //= n 

    digit_10.append(a)
    digit_10.reverse()
    
    return digit_10

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

class Natural_number:
    def question(self):
        self.select = np.random.randint(5)  
        self.n1 = np.random.randint(100)
        self.n2 = np.random.randint(100)     
        self.n3 = np.random.randint(low = 2, high = 10)
        self.n4 = np.random.randint(low = 2, high = 30)
        
        if self.select == 0:
            print ('{}가 소수인지 판별하고, 소수가 아니면, 약수를 구해라.'.format(self.n1))
        elif self.select ==1:
            print ('{}와 {}의 최대공약수를 구하여라.'.format(self.n1, self.n2))
        elif self.select ==2: 
            print ('{}와 {}의 최소공배수를 구하여라.'.format(self.n3, self.n4))
        elif self.select == 3:
            print ('{}를 2진법으로 나타내어라.'.format(self.n1))
        elif self.select == 4:
            self.n4_2 = digit_expand(self.n4, 2)
#            print '2진수 %i를 10진법으로 나타내어라.' %self.n4
            print ('2진수 [{}]를 10진법으로 나타내어라.'.format(', '.join(map(str, self.n4_2))))
            
    def answer(self):
        if self.select == 0:
            if is_prime2(self.n1):
                print ('{} 는 소수이다.'.format(self.n1))
            else:
                print (factorization(self.n1))
        elif self.select == 1:
            print (greatest_common_factor(self.n1,self.n2, show = True))
        elif self.select == 2:
            print (least_common_multiple(self.n3, self.n4))
        elif self.select == 3:
            print (digit_expand(self.n1, 2))
        elif self.select == 4:
            print (digit_expand(self.n4, 10))
            
    
q1 = Natural_number()
q1.question()
q1.answer()

    
q2 = Natural_number()
q2.question()
q2.answer()