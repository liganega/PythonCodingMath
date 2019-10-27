from fractions import Fraction  
import numpy as np

class Rational_number:
    def question(self):
        self.constant = np.random.randint(low = -10, high = 10, size = 4)
        self.pm = np.random.randint(4)
        if self.pm == 0:
            print ('({}/{}) + ({}/{}) = ?' .format(self.constant[0],self.constant[1],self.constant[2],self.constant[3]))
        elif self.pm == 1:
            print ('({}/{}) - ({}/{}) = ?' .format(self.constant[0],self.constant[1],self.constant[2],self.constant[3]))
        elif self.pm == 2:
            print ('({}/{}) * ({}/{}) = ?' .format(self.constant[0],self.constant[1],self.constant[2],self.constant[3]))
        else:
            print ('({}/{}) / ({}/{}) = ?' .format(self.constant[0],self.constant[1],self.constant[2],self.constant[3]))
        
    def answer(self):
        if self.pm == 0:
            return Fraction(self.constant[0],self.constant[1]) + Fraction(self.constant[2],self.constant[3])
        elif self.pm == 1:
            return Fraction(self.constant[0],self.constant[1]) - Fraction(self.constant[2],self.constant[3])
        elif self.pm == 2:
            return Fraction(self.constant[0],self.constant[1]) * Fraction(self.constant[2],self.constant[3])
        else:
            return Fraction(self.constant[0],self.constant[1]) / Fraction(self.constant[2],self.constant[3])
        

q1 = Rational_number()
q1.question()
q1.answer()