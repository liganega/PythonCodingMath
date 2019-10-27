def intersection(a,b):
    c = []               
    for i in a:
        if i  in b:
            c.append(i)
    c.sort()
    return c

def random_exclusive(low, high, how_many):
    number = []                             # 난수의 집합을 우선 공집합으로 만들고
    while how_many > 0:                     # n이 0보다 클때까지 
        a = np.random.randint(low,high)     # 1부터 30까지의 난수를 만들어 a로 놓은다음
        if a not in number:                 # a가 number에 없으면
            number.append(a)                # number에 a를 추가하고
        how_many -= 1                       # n을 1 줄여라
    return number

print (random_exclusive(1,31,10))

def random_intersection(low, high, how_many):
    group_A = random_exclusive(low, high, how_many)
    group_B = random_exclusive(low, high, how_many)
    c = intersection(group_A, group_B)
    print ('그룹 A의 난수는 : {}'.format(group_A))
    print ('그룹 B의 난수는 : {}'.format(group_B))
    print ('그룹 A와 그룹 B의 교집합은 {}'.format(c))
    return c

print (random_intersection(1,31,10))