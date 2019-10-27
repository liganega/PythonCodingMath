
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

class StudentRecord:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        temp = 0

a = StudentRecord()
        
student1 = StudentRecord('김똑똑', 'abc@gmail.com', '01011112222')
student2 = StudentRecord('박한별', 'efg@gmail.com', '01011113333')

print (student1.name)

print (student1.temp)