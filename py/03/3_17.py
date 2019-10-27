from fractions import Fraction
import numpy as np

a = [1,5,20] 
b = [Fraction(1,2), Fraction(1,3), 4]
c = b*2
c

a = np.array(a)
b = np.array(b)
c = b*2
c

d = a-c
y = Fraction(d[2], d[1])
x = Fraction((a[2]-a[1]*y),a[0])
print (x, y)

def simultaneous_eq(a,b):
    a = np.array(a)
    b = np.array(b)
    c = b* Fraction(a[0],b[0])
    d = a - c
    y = Fraction(d[2],d[1])
    x = Fraction(a[2]-a[1]*y,a[0])
    return x, y

a = [5,2,14]
b = [2,1,4]
x, y = simultaneous_eq(a,b)
print (x, y)

a = [2, 3, 4]   
b = [3, -4, -4]
x, y = simultaneous_eq(a,b)
print (x, y)

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

a = [1,3,4]
b = [5,0,-10]
simultaneous_eq(a,b)

def simultaneous_eq(a,b):
    if (a[0]/b[0]) == (a[1]/b[1]) != (a[2]/b[2]):
        print ('해는 없다')
        return None, None
    elif (a[0]/b[0]) == (a[1]/b[1]) == (a[2]/b[2]):
        print ('해는 무수히 많다')
        return None, None
    else:
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


class Linear_equation:
    def question(self):        
        self.number = np.random.randint(-10,10, size = 6)   
        print ('다음 연립방정식을 푸시오')
        print ('{}x + {}y = {}' .format(self.number[0],  self.number[1], self.number[2]))
        print ('{}x + {}y = {}' .format(self.number[3],  self.number[4], self.number[5]))
  
    def answer(self):
        a = [self.number[0], self.number[1], self.number[2]]
        b = [self.number[3], self.number[4], self.number[5]]
        x, y = simultaneous_eq(a,b)
        return x, y

q1 = Linear_equation()
q1.question()
q1.answer()