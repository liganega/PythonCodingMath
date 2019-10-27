import itertools
import numpy as np


x = ['x']*15
o = ['o']*5

n = len(list(itertools.permutations(x+o,3)))
count_no_o = 0
cpunt_one_o = 0
for i in list(itertools.permutations(x+o,3)):
    if 'o' not in i:
        count_no_o += 1
print ('3개 모두 당첨제비가 아닐 확률 : {}'.format(count_no_o/n))
print ('적어도 1개가 당첨제비일 확률 : {}'.format(1-count_no_o/n))
print (91/228)