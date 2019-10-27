import itertools
import numpy as np

count = 0
for i in list(itertools.permutations([1,2,3,4,5],5)):
    loc_1 = i.index(1)
    loc_2 = i.index(2)
    loc_3 = i.index(3)
    if (loc_1 < loc_2) and (loc_3 > loc_2):
        count += 1
print (count)