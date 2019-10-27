
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

class StudentRecord:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def math(self, score):
        self.math_score = score
    def english(self, score):
        self.english_score = score
    def show(self):
        print ('{}의 수학 성적은 {}, 영어 성적은 {}이다.'.format(self.name, self.math_score, self.english_score))
    def grade_both(self):
        if np.average([self.math_score, self.english_score]) >= 90:
            self.grade = 'A'
        elif np.average([self.math_score, self.english_score]) >= 80:
            self.grade = 'B'
        else:
            self.grade = 'C'
        return self.grade
    
    
student1 = StudentRecord('김똑똑', 'abc@gmail.com', '01011112222')
student2 = StudentRecord('박한별', 'efg@gmail.com', '01011113333')
student1.math(70)
student1.english(85)
student2.math(90)
student2.english(80)
student1.show()
student2.show()

print ('{}의 최종 성적은 {}'.format(student1.name, student1.grade_both()))
print ('{}의 최종 성적은 {}'.format(student2.name, student2.grade_both()))