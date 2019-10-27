import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction


def simultaneous_eq(a,b):
    if a[0] == 0:
        y = Fraction(a[2], a[1])
        x = Fraction(b[2] - b[1]*y, b[0])
    elif a[1] == 0:
        x = Fraction(a[2], a[0])
        y = Fraction(b[2] - b[0]*x, b[1])
    elif b[0] == 0:
        y = Fraction(b[2], b[1])
        x = Fraction(a[2] - a[1]*y, a[0])
    elif b[1] == 0:
        x = Fraction(b[2], b[0])
        y = Fraction(a[2] - a[0]*x, a[1])
    else:
        a = np.array(a)
        b = np.array(b)
        c = b* Fraction(a[0],b[0])
        d = a - c
        y = Fraction(d[2],d[1])
        x = Fraction(a[2]-a[1]*y,a[0])
    return x, y


class Linear_function:
    def question(self):
        self.select = np.random.randint(2)
        if self.select == 1:
            self.coefficient = np.random.randint(low = -10, high = 10, size = 2)
            self.constant = np.random.randint(low = -10, high = 10)
            print ('{}x + {}y + {} = 0 의, 기울기, x 절편, y 절편을 구하시오'.format(self.coefficient[0], self.coefficient[1], self.constant))
            print ('x는 -10 부터 10까지일때 위 함수를 그리시오.')
        else:
            self.coefficient = np.random.randint(low = -10, high = 10, size = 4)
            self.constant = np.random.randint(low = -10, high = 10, size = 2)
            print ('다음 두 직선의 교차점을 구하고, 두 그래프를 그리시오.')
            print ('{}x + {}y + {} = 0'.format(self.coefficient[0], self.coefficient[1], self.constant[0]))
            print ('{}x + {}y + {} = 0'.format(self.coefficient[2], self.coefficient[3], self.constant[1]))
               
    def answer(self):
        if self.select == 1:
            slope = Fraction(-self.coefficient[0], self.coefficient[1])
            y_cross = Fraction(-self.constant, self.coefficient[1])
            print ('기울기 : {}'.format(Fraction(-self.coefficient[0], self.coefficient[1])))
            print ('x절편 : {}'.format(Fraction(-self.constant, self.coefficient[0])))
            print ('y절편 : {}'.format(Fraction(-self.constant, self.coefficient[1])))
            x = np.arange(-10,11)
            y = slope*x + y_cross
            plt.plot(x,y)
            plt.grid()
        else:
            a = self.coefficient[0], self.coefficient[1], -self.constant[0]
            b = self.coefficient[2], self.coefficient[3], -self.constant[1]
            x, y = simultaneous_eq(a,b)
            print (x,y)
            x = np.arange(-10,11)
            slope1 = Fraction(-self.coefficient[0], self.coefficient[1])
            y_cross1 = Fraction(-self.constant[0], self.coefficient[1])
            
            slope2 = Fraction(-self.coefficient[2], self.coefficient[3])
            y_cross2 = Fraction(-self.constant[1], self.coefficient[3])
            y1 = slope1*x + y_cross1
            y2 = slope2*x + y_cross2
            plt.plot(x,y1)
            plt.plot(x,y2)
            plt.grid()

q1 = Linear_function()
q1.question()
q1.answer()