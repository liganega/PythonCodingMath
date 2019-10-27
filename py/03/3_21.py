import numpy as np

class Inequality:
    def __init__(self):
        print ('x는 -10부터 10까지의 정수이다. 다음 부등식을 만족하는 x를 구하시오.')
        
    def question(self):
        self.coefficient = 0
        self.constant = np.random.randint(low = -10, high = 10, size = 2)
        while self.coefficient == 0:
            self.coefficient = np.random.randint(low = -10, high = 10)
        self.a = np.random.randint(4, size = 1)
        
        if np.random.randint(2) == 0:
            self.symbol1 = '+'
        else:
            self.symbol1 = '-'
            
        if self.a % 4 == 0:
            self.symbol2 = '>'
        elif self.a % 4 == 1:
            self.symbol2 = '>='
        elif self.a % 4 == 2:
            self.symbol2 = '<='
        elif self.a % 4 == 3:
            self.symbol2 = '<'
    
        print ('{}x {} {} {} {} '.format(self.coefficient, self.symbol1, self.constant[0], self.symbol2, self.constant[1]))

    def answer(self):
        if self.symbol1 == '-':
            self.constant[0] *= -1
        
        if self.a % 4 == 0:
            y = list(filter(lambda a: self.coefficient*a + self.constant[0] > self.constant[1],  np.arange(-10,11,1)))
        elif self.a % 4 == 1:
            y = list(filter(lambda a: self.coefficient*a + self.constant[0] >= self.constant[1],  np.arange(-10,11,1)))
        elif self.a % 4 == 2:
            y = list(filter(lambda a: self.coefficient*a + self.constant[0] <= self.constant[1],  np.arange(-10,11,1)))
        elif self.a % 4 == 3:
            y = list(filter(lambda a: self.coefficient*a + self.constant[0] < self.constant[1],  np.arange(-10,11,1)))
        print (y)
        
q1 = Inequality()
q1.question()
q1.answer()