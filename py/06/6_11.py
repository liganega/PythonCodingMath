import numpy as np
import matplotlib.pyplot as plt

def second_order_direct(a,b,c):
    if b**2 - 4*a*c < 0:
        print ('No answer')
    else:
        x1 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2

print (second_order_direct(1,-2,1))
print (second_order_direct(3,-3,0))
print (second_order_direct(4,0,-4))

class Second_order:
    def __init__(self):
        print ('완전 제곱식을 이용하여 다음 이차방정식을 푸시오.')
    def question(self):
        self.d = 0
        while self.d == 0:
            self.d, self.e, self.f, self.g = np.random.randint(-5, 6, size = 4)
        self.a = self.d * self.f
        self.b = self.e * self.f + self.d * self.g
        self.c = self.e * self.g
        print ('{}x^2 + {}x + {} = 0'.format(self.a, self.b, self.c))
        
    def answer(self):
        if self.b**2 - 4*self.a*self.c < 0:
            print ('No answer')
        else:
            x1 = (-self.b + np.sqrt(self.b**2 - 4*self.a*self.c)) / (2*self.a)
            x2 = (-self.b - np.sqrt(self.b**2 - 4*self.a*self.c)) / (2*self.a)
        return x1, x2
    
a = Second_order()
a.question()
a.answer()