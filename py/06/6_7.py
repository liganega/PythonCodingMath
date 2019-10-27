
import numpy as np
import matplotlib.pyplot as plt

class Second_order_eq:
    def __init__(self):
        print ('x = {-5 부터 5까지의 정수} 다음을 이차방정식의 문제를 푸시오.')
    def question(self):
        self.c, self.d = np.random.randint(low = -5, high = 5, size = 2)
        self.a = self.c + self.d
        self.b = self.c * self.d
        print ('x^2 + {}x + {} = 0'.format(self.a, self.b))
        
    def answer(self):
        print ('x = {}, {}'.format(-self.c, -self.d))
        
a = Second_order_eq()
a.question()
a.answer()