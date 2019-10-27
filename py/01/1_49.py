import numpy as np

class Sets():   # 집합의 class인 sets를 정의
    def question(self):
        self.select = np.random.randint(3)  # 0이면 교집합, 1이면 합집합, 2이면 차집합을 계산하는 0,1,2중 하나의 숫자를 발생
        n_a = np.random.randint(10)    # list a의 갯수를 0~10 중 하나 발생
        n_b = np.random.randint(10)    # list b의 갯수를 0~10 중 하나 발생
        
        self.a = []
        self.b = []
        for i in np.arange(n_a):  # 중복되지 않는 n_a 갯수를 가진 집합 a를 생성
            temp = np.random.randint(10)
            if temp not in self.a:
                self.a.append(temp)
                
        for i in np.arange(n_b):  # 중복되지 않는 n_b 갯수를 가진 집합 a를 생성
            temp = np.random.randint(10)
            if temp not in self.b:
                self.b.append(temp)
        print ('a: [{}]'.format(','.join(map(str, self.a))))     
        print ('b: [{}]'.format(','.join(map(str, self.b))))   
        #print('a: [%s]' % ', '.join(map(str, self.a)))
        #print('b: [%s]' % ', '.join(map(str, self.b)))
        #print(*L, sep=', ')
        if self.select == 0:
            print ('a, b가 위와 같고 두 집합의 교집합을 구하시오')
        elif self.select == 1:
            print ('a, b가 위와 같고 두 집합의 합집합을 구하시오')
        elif self.select == 2:
            print ('a, b가 위와 같고 차집합 a-b를 구하시오')
                
    def setdata(self,a,b):
        self.a = a
        self.b = b
        
    def intersection(self):   # 집합을 class sets로 정의하고 그 중 교집합구하는 함수를 정의
        result = []
        for i in self.a:
            if i  in self.b:
                result.append(i)
        return result
    
    def union(self):
        result = self.b + []
        for i in self.a:  # a에 속한 모든 요소 i에 대해서 순서대로 실행시키자. 
            if i not in self.b:   # 만약 i가 b에 속하지 않는다면
                result.append(i) 
        return result
    
    def complement(self):
        result = self.a + []
        for i in self.b:   # a에 속한 모든 요소 i에 대해서 순서대로 실행시키자. 
            if i in self.a:   #i가 a에 속한다면
                result.remove(i)  #a에서 i를 지워라
        return result
    
    def answer(self):
        if self.select == 0:
            result = self.intersection()
            result.sort()
            print (result)
        elif self.select == 1:
            result = self.union()
            result.sort()
            print (result)
        elif self.select == 2:
            result = self.complement()
            result.sort()
            print (result)

q1 = Sets()
q1.question()
q1.answer()