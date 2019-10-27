import numpy as np

class Integer:
    def question(self):
        self.constant = np.random.randint(low = -10, high = 10, size = 2)
        self.pm = np.random.randint(5)
        self.exponent = np.random.randint(low = 2, high = 4)
        if self.pm == 0:
            print ('{} + {} = ?' .format(self.constant[0],  self.constant[1]))
        elif self.pm == 1:
            print ('{} - {} = ?' .format(self.constant[0],  self.constant[1]))
        elif self.pm == 2:
            print ('{} x {} = ?' .format(self.constant[0],  self.constant[1]))
        elif self.pm == 3:
            print ('{} / {} = ?' .format(self.constant[0],  self.constant[1]))
        else:
            print ('{}^{} = ?' .format(self.constant[0],  self.exponent))
            
    def answer(self):
        if self.pm == 0:
            return self.constant[0] + self.constant[1]
        elif self.pm == 1:
            return self.constant[0] - self.constant[1]
        elif self.pm == 2:
            return self.constant[0] * self.constant[1]
        elif self.pm == 3:
            return self.constant[0] / self.constant[1]
        else:
            return self.constant[0] ** self.exponent
        
q1 = Integer()
q1.question()
q1.answer()