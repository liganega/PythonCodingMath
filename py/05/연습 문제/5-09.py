import itertools

event = list(itertools.combinations([0,0,1,1,1,2,2,3,4,5], 3))
print (len(event))

event2 = list(itertools.combinations([1,1,1,2,2,3,4,5], 3))
print (len(event2))