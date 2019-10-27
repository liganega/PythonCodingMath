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

d = [-x for x in range(1,101) if is_prime2(x)]
print (d)