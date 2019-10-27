import itertools
import numpy as np

total = []  # 금액 합계의 list

a500 = np.arange(0,1600,500)
a100 = np.arange(0,800,100)
a50 = np.arange(0,110,50)
a10 = np.arange(0,70,10)

print (a500, a100, a50, a10)

total = list(itertools.product(a500, a100, a50, a10))
event = []
for i in total:
    if sum(i) not in event:
        event.append(sum(i))
print (len(event))