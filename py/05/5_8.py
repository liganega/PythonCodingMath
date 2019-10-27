import itertools

event = list(itertools.permutations(range(1,6), 2))
print (event)
print (len(event))