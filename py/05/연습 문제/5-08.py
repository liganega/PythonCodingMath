import itertools

total = list(itertools.product(range(1,7), range(1,7), range(1,7), range(1,7), range(1,7)))
sum5 = 0
for i in total:
    if sum(i) == 15:
        sum5 +=1
sum5