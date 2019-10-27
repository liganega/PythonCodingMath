import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

a = {'name' : '철수', 'age' : 15, 'hobby' : 'baseball'}
print (a)
print (a['name'])
print (a['age'])
print (a['hobby'])

a['phone'] = '01022223333'
print (a)

del a['phone']
print (a)
print ('')

print (a.keys())
print (a.values())
print (list(a.keys()))
print (tuple(a.values()))
print ('')

print (a['phone'])

print (a.get('phone'))

a.get('phone') == None

print (a.get('age'))
print ('')

print ('age' in a)
print ('phone' in a)