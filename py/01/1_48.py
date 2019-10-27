class Sets():                  # 집합의 연산을 Sets이라는 이름의 class로 정의
    def setdata(self,a,b):     # class의 def는 코딩함수가 아니라 매써드 (method)라고 부르며
                               # method는 입력값으로 항상 self를 맨 앞에 써 줘야함 
        self.a = a             # a를 class의 객체변수로 만든다.
        self.b = b             # b를 class의 객체변수로 만든다.
    
    def union(self):           # 합집합을 구하는 매써드
        result = self.b + []
        for i in self.a:  
            if i not in self.b:    
                result.append(i) 
        result.sort()
        return result
    
    def intersection(self):    # 교집합을 구하는 매써드
        result = []
        for i in self.a:
            if i  in self.b:
                result.append(i)
        result.sort()
        return result
    
    def complement(self):      # 차집합을 구하는 매써드
        result = self.a + []
        for i in self.b:    
            if i in self.a:    
                result.remove(i)   
        result.sort()
        return result
    
a = [1,3,4,5,6]
b = [2,4,6,3,0]

c = Sets()                
c.setdata(a,b)             

print (c.a, c.b)          
print ('{}와 {}의 합집합은 {}이다.'.format(c.a, c.b, c.union()))          
print ('{}와 {}의 교집합은 {}이다.'.format(c.a, c.b, c.intersection()))   
print ('{}와 {}의 차집합은 {}이다.'.format(c.a, c.b, c.complement()))    


a = ['apple', 'banana', 'melon', 'mango', 'tomato']
b = ['watermelon', 'strawberry', 'orange', 'apple', 'banana']

d = Sets()
d.setdata(a,b)

print (d.a, d.b)          
print (d.union())          
print (d.intersection())   
print (d.complement())     