import itertools

def is_prime2(a):
    b = range(2, a)  #2부터 a-1까지의 list
    c = 0
    for i in b:    
        if a % i == 0:  
            c += 1   
    if c > 0:
        d = False   
    else:
        d = True
    return d

add_prime = []
for i in range(1,7):
    for j in range(1,7):
        if is_prime2(i + j):
            add_prime.append((i,j))
print (add_prime)

n = len(add_prime)
p = Fraction(n,36)
print (n)
print (p)
print ('')

total = list(itertools.product([1,2,3,4,5,6], [1,2,3,4,5,6])) 
a = [i for i in total if is_prime2(sum(i))]
print (a)
print (Fraction(len(a), len(total)))